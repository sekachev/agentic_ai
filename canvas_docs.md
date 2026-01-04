JSON Canvas Spec
Version 1.0 — 2024-03-11

Top level
The top level of JSON Canvas contains two arrays:

nodes (optional, array of nodes)
edges (optional, array of edges)
Nodes
Nodes are objects within the canvas. Nodes may be text, files, links, or groups.

Nodes are placed in the array in ascending order by z-index. The first node in the array should be displayed below all other nodes, and the last node in the array should be displayed on top of all other nodes.

Generic node
All nodes include the following attributes:

id (required, string) is a unique ID for the node.
type (required, string) is the node type.
text
file
link
group
x (required, integer) is the x position of the node in pixels.
y (required, integer) is the y position of the node in pixels.
width (required, integer) is the width of the node in pixels.
height (required, integer) is the height of the node in pixels.
color (optional, canvasColor) is the color of the node, see the Color section.
Text type nodes
Text type nodes store text. Along with generic node attributes, text nodes include the following attribute:

text (required, string) in plain text with Markdown syntax.
File type nodes
File type nodes reference other files or attachments, such as images, videos, etc. Along with generic node attributes, file nodes include the following attributes:

file (required, string) is the path to the file within the system.
subpath (optional, string) is a subpath that may link to a heading or a block. Always starts with a #.
Link type nodes
Link type nodes reference a URL. Along with generic node attributes, link nodes include the following attribute:

url (required, string)
Group type nodes
Group type nodes are used as a visual container for nodes within it. Along with generic node attributes, group nodes include the following attributes:

label (optional, string) is a text label for the group.
background (optional, string) is the path to the background image.
backgroundStyle (optional, string) is the rendering style of the background image. Valid values:
cover fills the entire width and height of the node.
ratio maintains the aspect ratio of the background image.
repeat repeats the image as a pattern in both x/y directions.
Edges
Edges are lines that connect one node to another.

id (required, string) is a unique ID for the edge.
fromNode (required, string) is the node id where the connection starts.
fromSide (optional, string) is the side where this edge starts. Valid values:
top
right
bottom
left
fromEnd (optional, string) is the shape of the endpoint at the edge start. Defaults to none if not specified. Valid values:
none
arrow
toNode (required, string) is the node id where the connection ends.
toSide (optional, string) is the side where this edge ends. Valid values:
top
right
bottom
left
toEnd (optional, string) is the shape of the endpoint at the edge end. Defaults to arrow if not specified. Valid values:
none
arrow
color (optional, canvasColor) is the color of the line, see the Color section.
label (optional, string) is a text label for the edge.
Color
The canvasColor type is used to encode color data for nodes and edges. Colors attributes expect a string. Colors can be specified in hex format e.g. "#FF0000", or using one of the preset colors, e.g. "1" for red. Six preset colors exist, mapped to the following numbers:

"1" red
"2" orange
"3" yellow
"4" green
"5" cyan
"6" purple
Specific values for the preset colors are intentionally not defined so that applications can tailor the presets to their specific brand colors or color scheme.


sample 

{
	"nodes":[
		{"id":"754a8ef995f366bc","type":"group","x":-300,"y":-460,"width":610,"height":200,"label":"JSON Canvas"},
		{"id":"8132d4d894c80022","type":"file","file":"readme.md","x":-280,"y":-200,"width":570,"height":560,"color":"6"},
		{"id":"7efdbbe0c4742315","type":"file","file":"_site/logo.svg","x":-280,"y":-440,"width":217,"height":80},
		{"id":"59e896bc8da20699","type":"text","text":"Learn more:\n\n- [Apps](/docs/apps.md)\n- [Spec](spec/1.0.md)\n- [Github](https://github.com/obsidianmd/jsoncanvas)","x":40,"y":-440,"width":250,"height":160},
		{"id":"0ba565e7f30e0652","type":"file","file":"spec/1.0.md","x":360,"y":-400,"width":400,"height":400}
	],
	"edges":[
		{"id":"6fa11ab87f90b8af","fromNode":"7efdbbe0c4742315","fromSide":"right","toNode":"59e896bc8da20699","toSide":"left"}
	]
}