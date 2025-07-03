# OpenAPI Client Templates

This directory contains custom templates for openapi-python-client generator. These templates ensure that generated code maintains consistency with the existing codebase structure.

## Usage

The templates in this directory are used by the GitHub Action workflow to generate client code that matches our project's style and structure.

## Template Structure

- `api_client`: Templates for API client classes
- `endpoint_module`: Templates for endpoint modules
- `model`: Templates for data models
- `types`: Templates for type definitions

Each template follows the Jinja2 format used by openapi-python-client. 