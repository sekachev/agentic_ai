# Source: https://mszturc.github.io/obsidian-advanced-slides/layout

Advanced Slides provides a variety of components that simplify layouting of you slides:

By using the <split> tag you are able to split the content of your slide in rows and columns Attributes even By setting the even attribute the Content of the split element gets divided evenly: <split even> ![](https://picsum.photos/id/1005/250/250) ![](https://picsum.photos/id/1010/250/250) ![](https://picsum.photos/id/1025/250/250) </split> Example: In a split with 3 children every child takes 1/3 of the availible width of the slide gap By adding the gap attribute there will be a gap between each element:

By using the <grid> tag you are able to layout the content of your slide in parts. Concept Grid layouts drag-and-drop is used to size and position content of your slides. Drag to size a block of content on your slide, then Drop to position that block anywhere on the slide. Basic Syntax The following syntax is used to drag-and-drop a grid in Advanced Slides: <grid drag="width height" drop="x y"> The width and height values of the drag property define the size of the area in which the content will be displayed.