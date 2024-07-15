# Rest-API Plugin

The Rest-API plugin facilitates the use of the AaC application through a `RESTful API` interface. A `RESTful API` is an architectural style where an application interface sends and receives data through HTTP requests.

## Help command for Rest-API

The section below is an example of the terminal output for the -h flag.

```bash
$ aac rest-api -h
Usage: aac rest-api [OPTIONS]

Options:
  --host TEXT     Set the hostname of the service. Useful for operating behind
                  proxies.  [default: 0.0.0.0]
  --port INTEGER  The port to which the RESTful service will be bound.
                  [default: 8080]
  -h, --help      Show this message and exit.
```

## RESTful API
### Request Contents
A request to the HTTP server contains a request method.
The four request methods used by the interface are:

- `GET`, which receives and reads data.
- `PUT`, which updates data that already exists on the server.
- `POST`, which creates data.
- `DELETE`, which removes data.

A `RESTful API` request also needs to contain a unique resource identifier which contains a path to the resource that the method is acting on.

### Response Contents

The two parts of a response from a HTTP server are the response status, and the message body.

The four most common response statuses are:

- `200 OK`
    - This indicates that a request has succeeded
- `204 No Content`
    - This indicates that a request succeeded, but there was no data for the client to receive.
- `400 Bad Request`
    - This indicates that the server could not understand the request, and is usually caused by incorrect syntax
- `404 Not Found`
    - This indicates that the server could not find a resource with the given unique resource identifier.

Message bodies will contain the data requested by a GET command in either a JSON or XML format.

## Request Method Commands

### Request Method Argument Types

Some request method commands require parameter arguments.  In order for arguments to be accepted by the RESTful API, they have to derive from a type called `BaseModel`.  Included in this plugin are several `BaseModel` derived types corresponding to objects used by the AaC Application.  When passing AaC objects as arguments, they must first be converted to one of the derived types.  Listed below are several AaC types and their corresponding `BaseModel` types, along with an included Python method to convert the two.

`AacCommand` -> `CommandModel`
```python
CommandModel = to_command_model(AaCCommand)
```

`AacCommandArgument` -> `CommandArgumentModel`
```python
CommandArgumentModel = to_command_argument_model(AacCommandArgument)
```

`Definition` -> `DefinitionModel`
```python
DefinitionModel = to_definition_model(Definition)
Definition = to_definition_class(DefinitionModel)
```

`AaCFile` -> `FileModel`
```python
FileModel = to_file_model(AaCFile)
AaCFile = to_file_class(FileModel)
```

Other included BaseModel types that do not correspond to specific AaC types are:

`CommandRequestModel`
    - A class which contains a command name and a list of arguments
`FilePathModel`
    - A class which contains a file uri.
`FilePathRenameModel`
    - A class for renaming a file, which contains a file uri to replace with the new file uri.


### Available Request Method Commands

The requests available to be sent using the REST-API plugin are listed below.  These examples use the request method with the unique resource identifier as the first argument, followed by any other required arguments of the method.  The section under each command will contain the desired response status.

```python
get("/files/context")
```
HTTPStatus: `200 OK`
This command reads and returns a list of files in the current `LanguageContext`.

```python
get("/files/available")
```
HTTPStatus: `200 OK`
This command reads and returns a list of files in the workspace available for import into the active context. The list of files returned does not include files already in the context.

```python
get("/file", file_uri: str)
```
HTTPStatus: `200 OK`
This command accepts file uri as an argument and returns the requested file.

```python
post("/files/import", file_models: list[FilePathModel])
```
HTTPStatus: `NO_CONTENT`
This command imports a list of files into the `LanguageContext`.

```python
put("/file", rename_request: FilePathRenameModel)
```
HTTPStatus: `NO_CONTENT`
This command renames a file, or updates its uri.

```python
delete("/file", file_uri: str)
```
HTTPStatus: `NO_CONTENT`
This command removes the file from the active `LanguageContext`.

```python
get("/definitions")
```
HTTPStatus: `200 OK`
This command returns a list of definitions in the active `LanguageContext`.

```python
get("/definition", name: str)
```
HTTPStatus: `200 OK`
This command accepts a definition name as a string, and returns a list of definitions with that name.

```python
post("/definition", definition_model: DefinitionModel)
```
HTTPStatus: `NO_CONTENT`
This command Adds a definition to the active `LanguageContext`.

```python
post("/definitions", definition_models: list[DefinitionModels])
```
HTTPStatus: `NO_CONTENT`
This command Adds a list of definitions the the active `LanguageContext`.

```python
put("/definition", definition_model: DefinitionModel)
```
HTTPStatus: `NO_CONTENT`
This command updates a definition in the active `LanguageContext`.

```python
delete("/definition", name: str)
```
HTTPStatus: `NO_CONTENT`
This command removes a definition from the active `LanguageContext`.

```python
get("/context/schema", key: str)
```
HTTPStatus: `OK`
This command takes in a root key and returns the corresponding root YAML schema.

```python
get("/context/root_keys")
```
HTTPStatus: `OK`
This command returns a list of root keys from the active `LanguageContext`.

```python
get("/command")
```
HTTPStatus: `OK`
Returns a list of all available commands.

```python
post("/command", command_request: CommandRequestModel)
```
HTTPStatus: `OK`
This command executes the given AaC command.

## Gen-openapi-spec Command

### Help command for gen-openapi-spec

```bash
$ aac gen-openapi-spec -h
Usage: aac gen-openapi-spec [OPTIONS] OUTPUT_DIRECTORY

Options:
  -h, --help  Show this message and exit.
```

### Gen-openapi-spec usage and return

The `gen-openapi-spec` command returns a JSON file containing the open API schema. Below is an example of a successful run of the command.

```bash
$ aac gen-openapi-spec ./output_directory
Successfully wrote the OpenAPI spec to ./output_directory/AaC_OpenAPI_Schema.json.
```

Executing the above command will create a file in `./output_directory` called `AaC_OpenAPI_Schema.json`, which will contain the API schema in a JSON format.

![Created File](../images/openapi.png)


