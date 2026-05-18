"""Auto-generated from https://ai.google.dev/gemini-api/docs/text-generation. Do not edit manually."""

from gemini_docs.models import GeminiDoc

SLUG = 'text-generation'
TITLE = 'Text Generation'
SOURCE_URL = 'https://ai.google.dev/gemini-api/docs/text-generation'
MODULE_NAME = 'text_generation'
MARKDOWN_FILENAME = 'text-generation-gemini.md'
MARKDOWN = 'The Gemini API can generate text output from text, images, video, and audio\ninputs.\n\nHere\'s a basic example:\n\n[]()\n\n## Thinking with Gemini\n\nGemini models often have ["thinking"](https://ai.google.dev/gemini-api/docs/thinking) enabled by default\nwhich allows the model to reason before responding to a request.\n\nEach model supports different thinking configurations which gives you control\nover cost, latency, and intelligence. For more details, see the\n[thinking guide](https://ai.google.dev/gemini-api/docs/thinking#set-budget).\n\n## System instructions and other configurations\n\nYou can guide the behavior of Gemini models with system instructions. To do so,\npass a [`GenerateContentConfig`](https://ai.google.dev/api/generate-content#v1beta.GenerationConfig)\nobject.\n\nThe [`GenerateContentConfig`](https://ai.google.dev/api/generate-content#v1beta.GenerationConfig)\nobject also lets you override default generation parameters, such as\n[temperature](https://ai.google.dev/api/generate-content#v1beta.GenerationConfig).\n\nWhen using Gemini 3 models, we strongly recommend keeping the `temperature` at its default value of 1.0. Changing the temperature (setting it below 1.0) may lead to unexpected behavior, such as looping or degraded performance, particularly in complex mathematical or reasoning tasks.\n\nRefer to the [`GenerateContentConfig`](https://ai.google.dev/api/generate-content#v1beta.GenerationConfig)\nin our API reference for a complete list of configurable parameters and their\ndescriptions.\n\n## Multimodal inputs\n\nThe Gemini API supports multimodal inputs, allowing you to combine text with\nmedia files. The following example demonstrates providing an image:\n\nFor alternative methods of providing images and more advanced image processing,\nsee our [image understanding guide](https://ai.google.dev/gemini-api/docs/image-understanding).\nThe API also supports [document](https://ai.google.dev/gemini-api/docs/document-processing), [video](https://ai.google.dev/gemini-api/docs/video-understanding), and [audio](https://ai.google.dev/gemini-api/docs/audio)\ninputs and understanding.\n\n## Streaming responses\n\nBy default, the model returns a response only after the entire generation \nprocess is complete.\n\nFor more fluid interactions, use streaming to receive [`GenerateContentResponse`](https://ai.google.dev/api/generate-content#v1beta.GenerateContentResponse) instances incrementally\nas they\'re generated.\n\n## Multi-turn conversations (chat)\n\nOur SDKs provide functionality to collect multiple rounds of prompts and\nresponses into a chat, giving you an easy way to keep track of the conversation\nhistory.\n\n**Note:** Chat functionality is only implemented as part of the SDKs. Behind the scenes, it still uses the [`generateContent`](https://ai.google.dev/api/generate-content#method:-models.generatecontent) API. For multi-turn conversations, the full conversation history is sent to the model with each follow-up turn.\n\nStreaming can also be used for multi-turn conversations.\n\n## Prompting tips\n\nConsult our [prompt engineering guide](https://ai.google.dev/gemini/docs/prompting-strategies) for\nsuggestions on getting the most out of Gemini.\n\n## What\'s next\n\n- Try [Gemini in Google AI Studio](https://aistudio.google.com).\n- Experiment with [structured outputs](https://ai.google.dev/gemini-api/docs/structured-output) for JSON-like responses.\n- Explore Gemini\'s [image](https://ai.google.dev/gemini-api/docs/image-understanding), [video](https://ai.google.dev/gemini-api/docs/video-understanding), [audio](https://ai.google.dev/gemini-api/docs/audio) and [document](https://ai.google.dev/gemini-api/docs/document-processing) understanding capabilities.\n- Learn about multimodal [file prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide).\n'

DOCUMENT = GeminiDoc(
    slug=SLUG,
    title=TITLE,
    source_url=SOURCE_URL,
    module_name=MODULE_NAME,
    markdown_filename=MARKDOWN_FILENAME,
    content=MARKDOWN,
)


def get_document() -> GeminiDoc:
    return DOCUMENT


def get_markdown() -> str:
    return MARKDOWN
