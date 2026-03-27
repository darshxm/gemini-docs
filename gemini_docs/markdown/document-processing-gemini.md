Gemini models can process documents in PDF format, using native
vision to understand entire document contexts. This goes beyond
just text extraction, allowing Gemini to:

- Analyze and interpret content, including text, images, diagrams, charts, and tables, even in long documents up to 1000 pages.
- Extract information into [structured output](https://ai.google.dev/gemini-api/docs/structured-output) formats.
- Summarize and answer questions based on both the visual and textual elements in a document.
- Transcribe document content (e.g. to HTML), preserving layouts and formatting, for use in downstream applications.

You can also pass non-PDF documents in the same way but Gemini will see them
as normal text which will eliminate context like charts or formatting.

## Passing PDF data inline

You can pass PDF data inline in the request to `generateContent`. This is best
suited for smaller documents or temporary processing where you don't need to
reference the file in subsequent requests. We recommend using the [Files API](https://ai.google.dev/gemini-api/docs/document-processing#large-pdfs)
for larger documents that you need to refer to in multi-turn interactions to
improve request latency and reduce bandwidth usage.

The following example shows you how to fetch a PDF from a URL and convert it to
bytes for processing:

### Python

    from google import genai
    from google.genai import types
    import httpx
    
    client = genai.Client()
    
    doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    
    # Retrieve and encode the PDF byte
    doc_data = httpx.get(doc_url).content
    
    prompt = "Summarize this document"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[
            types.Part.from_bytes(
                data=doc_data,
                mime_type='application/pdf',
            ),
            prompt
        ]
    )
    
    print(response.text)
    

You can also read a PDF from a local file for processing:

### Python

    from google import genai
    from google.genai import types
    import pathlib
    
    client = genai.Client()
    
    # Retrieve and encode the PDF byte
    filepath = pathlib.Path('file.pdf')
    
    prompt = "Summarize this document"
    response = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents=[
          types.Part.from_bytes(
            data=filepath.read_bytes(),
            mime_type='application/pdf',
          ),
          prompt])
    print(response.text)
    

## Uploading PDFs using the Files API

We recommend you use Files API for larger files or when you intend to reuse a
document across multiple requests. This improves request latency and reduces
bandwidth usage by decoupling the file upload from the model requests.

**Note:** The Files API is available at no cost in all regions where the Gemini API is available. Uploaded files are stored for 48 hours.

### Large PDFs from URLs

Use the File API to simplify uploading and processing large PDF files from URLs:

### Python

    from google import genai
    from google.genai import types
    import io
    import httpx
    
    client = genai.Client()
    
    long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
    
    # Retrieve and upload the PDF using the File API
    doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)
    
    sample_doc = client.files.upload(
      # You can pass a path or a file-like object here
      file=doc_io,
      config=dict(
        mime_type='application/pdf')
    )
    
    prompt = "Summarize this document"
    
    response = client.models.generate_content(
      model="gemini-3-flash-preview",
      contents=[sample_doc, prompt])
    print(response.text)
    

### Large PDFs stored locally

### Python

    from google import genai
    from google.genai import types
    import pathlib
    import httpx
    
    client = genai.Client()
    
    # Retrieve and encode the PDF byte
    file_path = pathlib.Path('large_file.pdf')
    
    # Upload the PDF using the File API
    sample_file = client.files.upload(
        file=file_path,
    )
    
    prompt="Summarize this document"
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[sample_file, "Summarize this document"])
    print(response.text)
    

You can verify the API successfully stored the uploaded file and get its
metadata by calling [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get). Only the `name`
(and by extension, the `uri`) are unique.

### Python

    from google import genai
    import pathlib
    
    client = genai.Client()
    
    fpath = pathlib.Path('example.txt')
    fpath.write_text('hello')
    
    file = client.files.upload(file='example.txt')
    
    file_info = client.files.get(name=file.name)
    print(file_info.model_dump_json(indent=4))
    

## Passing multiple PDFs

The Gemini API is capable of processing multiple PDF documents (up to 1000 pages)
in a single request, as long as the combined size of the documents and the text
prompt stays within the model's context window.

### Python

    from google import genai
    import io
    import httpx
    
    client = genai.Client()
    
    doc_url_1 = "https://arxiv.org/pdf/2312.11805"
    doc_url_2 = "https://arxiv.org/pdf/2403.05530"
    
    # Retrieve and upload both PDFs using the File API
    doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
    doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)
    
    sample_pdf_1 = client.files.upload(
      file=doc_data_1,
      config=dict(mime_type='application/pdf')
    )
    sample_pdf_2 = client.files.upload(
      file=doc_data_2,
      config=dict(mime_type='application/pdf')
    )
    
    prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[sample_pdf_1, sample_pdf_2, prompt]
    )
    
    print(response.text)
    

## Technical details

Gemini supports PDF files up to 50MB or 1000 pages. This limit applies
to both inline data and Files API uploads. Each document page is equivalent to 258
tokens.

While there are no specific limits to the number of pixels in a document besides
the model's [context window](https://ai.google.dev/gemini-api/docs/long-context), larger pages are
scaled down to a maximum resolution of 3072 x 3072 while preserving their original
aspect ratio, while smaller pages are scaled up to 768 x 768 pixels. There is no
cost reduction for pages at lower sizes, other than bandwidth, or performance
improvement for pages at higher resolution.

### Gemini 3 models

Gemini 3 introduces granular control over multimodal vision processing with the
`media_resolution` parameter. You can now set the resolution to low, medium, or
high per individual media part. With this addition, the processing of PDF
documents has been updated:

For more details about the media resolution parameter, see the
[Media resolution](https://ai.google.dev/gemini-api/docs/media-resolution) guide.

### Document types

Technically, you can pass other MIME types for document understanding, like
TXT, Markdown, HTML, XML, etc. However, document vision **only meaningfully
understands PDFs**. Other types will be extracted as pure text, and the model
won't be able to interpret what we see in the rendering of those files. Any
file-type specifics like charts, diagrams, HTML tags, Markdown formatting, etc.,
will be lost.

To learn about other file input methods, see the
[File input methods](https://ai.google.dev/gemini-api/docs/file-input-methods) guide.

### Best practices

For best results:

- Rotate pages to the correct orientation before uploading.
- Avoid blurry pages.
- If using a single page, place the text prompt after the page.

## What's next

To learn more, see the following resources:

- [File prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide): The Gemini API supports prompting with text, image, audio, and video data, also known as multimodal prompting.
- [System instructions](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions): System instructions let you steer the behavior of the model based on your specific needs and use cases.
