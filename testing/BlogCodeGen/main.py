import html

file = "example.cpp"

# Read the Python file
with open(file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Prefix and escape each line
prefixed_lines = []
for line in lines:
    escaped_line = html.escape(line.rstrip("\n"))
    prefixed_lines.append("&nbsp;&nbsp;" + escaped_line)

formatted_code = "\n".join(prefixed_lines)

# Wrap in HTML table and include filename
html_output = f"""<table width="99%" border="1">
<tr><td>&nbsp;&nbsp;<strong>{html.escape(file)}</strong></td></tr>
<tr><td>
<pre style="font-size: 12px;">
{formatted_code}
</pre>
</td></tr>
</table>
<br />"""

# Write to new HTML file
with open("out_" + file + ".txt", "w", encoding="utf-8") as f:
    f.write(html_output)

print("HTML file created: output.html")
