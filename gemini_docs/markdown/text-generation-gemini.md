**Note:** This version of the page covers the **Interactions API**. You can use the toggle on this page to switch to the [generateContent API version of this page](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding).

The Gemini API can generate text output from text, images, video, and audio
inputs.

Here's a basic example:

The Google GenAI SDKs provide convenience properties directly
on the returned `Interaction` object to access the model's response.

The most common helper is **`interaction.output_text`** (String), which returns
the last text blocks in the model's response. If the response is split
across multiple consecutive `TextContent` blocks, it automatically joins them.
Note that `.output_text` does not include earlier text blocks separated by
non-text content (such as thoughts, images, audio, or tool calls). For complex
or interleaved multimodal responses, you must manually iterate over `steps`
instead. To learn more about other media convenience properties, see the
[Interactions overview](https://ai.google.dev/gemini-api/docs/interactions#convenience-properties).

[]()

## Thinking with Gemini

Gemini models often have ["thinking"](https://ai.google.dev/gemini-api/docs/interactions/thinking)
enabled by default which allows the model to reason before responding to a
request.

Each model supports different thinking configurations which gives you control
over cost, latency, and intelligence. For more details, see the
[thinking guide](https://ai.google.dev/gemini-api/docs/interactions/thinking#set-budget).

## System instructions and other configurations

You can guide the behavior of Gemini models with system instructions. Pass
a `system_instruction` parameter to configure the model's behavior.

You can also override default generation parameters, such as
temperature, using the `generation_config` parameter.

Refer to the [Interactions API reference](https://ai.google.dev/api/interactions-api)
for a complete list of configurable parameters and their
descriptions.

## Multimodal inputs

The Gemini API supports multimodal inputs, allowing you to combine text with
media files. The following example demonstrates providing an image:

For alternative methods of providing images and more advanced image processing,
see our [image understanding guide](https://ai.google.dev/gemini-api/docs/interactions/image-understanding).
The API also supports [document](https://ai.google.dev/gemini-api/docs/interactions/document-processing), [video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding), and
[audio](https://ai.google.dev/gemini-api/docs/interactions/audio) inputs and understanding.

## Streaming responses

By default, the model returns a response only after the entire generation 
process is complete.

For more fluid interactions, use streaming to handle response chunks
as they're generated. For a comprehensive guide covering event types,
streaming with tools, thinking, agents, and image generation, see the
dedicated [Streaming interactions](https://ai.google.dev/gemini-api/docs/interactions/streaming)
guide.

## Multi-turn conversations

The Interactions API supports multi-turn conversations by chaining interactions
together using `previous_interaction_id`. Each turn is a separate interaction,
and the API automatically manages conversation history.

**Note:** Unlike other APIs where you might manage conversation history manually, the Interactions API handles conversation state server-side. You pass the `id` from the previous interaction to continue the conversation.

Streaming can also be used for multi-turn conversations by combining
`previous_interaction_id` with the streaming methods.

## Stateless conversations

By default, the Interactions API manages conversation state server-side when you use `previous_interaction_id`. However, you can also operate in stateless mode by managing the conversation history yourself on the client side.

To use stateless mode:
1. Set `store=false` in your request to opt out of server-side storage.
2. Maintain the conversation history as an array of **steps** on the client side.
3. In subsequent requests, pass the accumulated steps in the `input` field, and append your new turn as a `user_input` step.

**Note:** If the model uses "thinking" or tools, you **must** preserve and resend all model-generated steps (such as `thought` and `function_call` steps) exactly as received, as they contain signatures required to continue the conversation.

## Prompting tips

Consult our [prompt engineering guide](https://ai.google.dev/gemini/docs/prompting-strategies) for
suggestions on getting the most out of Gemini.

## What's next

- Try [Gemini in Google AI Studio](https://aistudio.google.com).
- Experiment with [structured outputs](https://ai.google.dev/gemini-api/docs/interactions/structured-output) for JSON-like responses.
- Explore Gemini's [image](https://ai.google.dev/gemini-api/docs/interactions/image-understanding), [video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding), [audio](https://ai.google.dev/gemini-api/docs/interactions/audio) and [document](https://ai.google.dev/gemini-api/docs/interactions/document-processing) understanding capabilities.
- Learn about multimodal [file prompting strategies](https://ai.google.dev/gemini-api/docs/interactions/files#prompt-guide).
