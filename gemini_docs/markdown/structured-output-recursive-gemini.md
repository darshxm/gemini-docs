**Note:** This version of the page covers the **Interactions API**. You can use the toggle on this page to switch to the [generateContent API version of this page](https://ai.google.dev/gemini-api/docs/generate-content/structured-output).

You can configure Gemini models to generate responses that adhere to a provided
JSON Schema. This ensures predictable, type-safe results and simplifies
extracting structured data from unstructured text.

Using structured outputs is ideal for:

- **Data extraction:** Pull specific information like names and dates from text.
- **Structured classification:** Classify text into predefined categories.
- **Agentic workflows:** Generate structured inputs for tools or APIs.

In addition to supporting JSON Schema in the REST API, the Google GenAI SDKs
allow defining schemas using
[Pydantic](https://docs.pydantic.dev/latest/) (Python) and
[Zod](https://zod.dev/) (JavaScript).

## Structured output examples

### Recipe Extractor

This example demonstrates how to extract structured data from text using basic
JSON Schema types like `object`, `array`, `string`, and `integer`.

**Example Response:**

### Content Moderation

This example showcases `anyOf` for conditional schemas and `enum` for
classification, allowing the output structure to vary based on the content.

**Example Response:**

### Recursive Structures

This example illustrates how to define a recursive schema such as an
organization chart.

**Example Response:**

## Streaming results

You can stream structured outputs, allowing you to start processing the
response as it's being generated. The streamed chunks are valid partial JSON
strings that can be concatenated to form the final JSON object.

## Structured outputs with tools

**Preview:** This feature is available only to Gemini 3 series models.

Gemini 3 lets you combine Structured Outputs with built-in tools, including
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search),
[URL Context](https://ai.google.dev/gemini-api/docs/url-context),
[Code Execution](https://ai.google.dev/gemini-api/docs/code-execution),
[File Search](https://ai.google.dev/gemini-api/docs/file-search#structured-output), and
[Function Calling](https://ai.google.dev/gemini-api/docs/function-calling).

## JSON schema support

To generate a JSON object, configure `response_format` with an object (or an array containing an object) of type `text` and set its `mime_type` to `application/json`. The schema should be provided in the `schema` field.

Gemini's structured output mode supports a subset of the
[JSON Schema](https://json-schema.org/) specification.

The following values of `type` are supported:

- **`string`**: For text.
- **`number`**: For floating-point numbers.
- **`integer`**: For whole numbers.
- **`boolean`**: For true or false values.
- **`object`**: For structured data with key-value pairs.
- **`array`**: For lists of items.
- **`null`**: To allow a property to be null, include `"null"` in the type array (e.g., `{"type": ["string", "null"]}`).

These descriptive properties help guide the model:

- **`title`**: A short description of a property.
- **`description`**: A longer and more detailed description of a property.

### Type-specific properties

**For `object` values:**

- **`properties`**: An object where each key is a property name and each value is a schema for that property.
- **`required`**: An array of strings, listing which properties are mandatory.
- **`additionalProperties`**: Controls whether properties not listed in `properties` are allowed. Can be a boolean or a schema.

**For `string` values:**

- **`enum`**: Lists a specific set of possible strings for classification tasks.
- **`format`**: Specifies a syntax for the string, such as `date-time`, `date`, `time`.

**For `number` and `integer` values:**

- **`enum`**: Lists a specific set of possible numeric values.
- **`minimum`**: The minimum inclusive value.
- **`maximum`**: The maximum inclusive value.

**For `array` values:**

- **`items`**: Defines the schema for all items in the array.
- **`prefixItems`**: Defines a list of schemas for the first N items, allowing for tuple-like structures.
- **`minItems`**: The minimum number of items in the array.
- **`maxItems`**: The maximum number of items in the array.

## Structured outputs versus function calling

## Best practices

- **Clear descriptions:** Use the `description` field to guide the model.
- **Strong typing:** Use specific types (`integer`, `string`, `enum`).
- **Prompt engineering:** Clearly state what you want the model to do.
- **Validation:** While output is syntactically correct JSON, always validate values in your application.
- **Error handling:** Implement robust error handling for schema-compliant but semantically incorrect outputs.

## Limitations

- **Schema subset:** Not all JSON Schema features are supported.
- **Schema complexity:** Very large or deeply nested schemas may be rejected.
