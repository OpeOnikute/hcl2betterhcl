# HCLToBetterHCL

This does a simple thing - removes the quotes from variables and block names in HCL. Encountered this problem when I used the [hcl2json](https://www.hcl2json.com/) site to convert from JSON to HCL. The output looks like this:

```
"definition" = {
    "legend_columns" = ["avg", "min", "max", "value", "sum"]
    "legend_layout" = "vertical"
    "markers" = []
}
```

This isn't valid HCL for Terraform 0.13+ as variables shouldn't have quotes and "=" for blocks, so I had to remove them. This tool removes the quotes and prints to stdout:
```
definition {
    legend_columns = ["avg", "min", "max", "value", "sum"]
    legend_layout = "vertical"
    markers = []
}
```

This is a very niche case, so if you have a use-case that deviates from the principles this was designed with, feel free to open an issue or a PR!

## Usage

- Clone this repository.
- Add the HCL you need to remove quotes from to `hcl.txt`.
- Run `python main.py` in the terminal.