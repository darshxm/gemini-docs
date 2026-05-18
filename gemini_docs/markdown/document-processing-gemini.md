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

You can also read a PDF from a local file for processing:

## Uploading PDFs using the Files API

We recommend you use Files API for larger files or when you intend to reuse a
document across multiple requests. This improves request latency and reduces
bandwidth usage by decoupling the file upload from the model requests.

**Note:** The Files API is available at no cost in all regions where the Gemini API is available. Uploaded files are stored for 48 hours.

### Large PDFs from URLs

Use the File API to simplify uploading and processing large PDF files from URLs:

### Large PDFs stored locally

You can verify the API successfully stored the uploaded file and get its
metadata by calling [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get). Only the `name`
(and by extension, the `uri`) are unique.

## Passing multiple PDFs

The Gemini API is capable of processing multiple PDF documents (up to 1000 pages)
in a single request, as long as the combined size of the documents and the text
prompt stays within the model's context window.

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
