# search-legal-headers

Look for legal text in your source files or whatever

## Usage

Add the following snippet to your workflow:

```yaml
- name: Search Legal Headers
  uses: nilp0inter/search-legal-headers@v0.0.2
```

## Configuration

Add a json file named `.legal.json` in the root of your repository with *file
patterns* and *strings* to search for.

```json
{
  "**/*.hs": "Licensed under the Apache License, Version 2.0 (the \"License\");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an \"AS IS\" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n",
  "LICENSE": "Apache License"
}
```
