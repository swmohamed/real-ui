# Interface Family: Spatial Canvas / Inspector

The primary object is a SPACE: a board, image, diagram, map, chart,
or model. Chrome inspects the selection. This is not a dashboard
of cards and not a docs tree.

Apply `interface-families/README.md`. This catalog never invents
infinite canvases, presence, layers, or CAD kernels.

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, wave 25)
plus prior corpus (Figma, Canva, Windy, earth.nullschool, Ventusky,
StoryMaps) and V6 DOC-OBSERVED Figma/Miro. Layout already names
`canvas + inspector` as a candidate organization; this file stores
WHEN that organization splits.

Invision's fetch returned Miro's page — contaminated, skip.

## Distinct problem space

Users: people who make or read a spatial artifact. Jobs: see the
whole, select a part, change it, keep structure inspectable.
Frequency varies. Consequence is a wrong mark on a shared board
or a missed aircraft.

WHEN NOT queue: there is no arriving ticket list as the home.
WHEN NOT docs: the page is not a TOC of prose. WHEN NOT live
essay: immersive-experimental story-maps remain stories first.
WHEN NOT asset-library: Photopea edits pixels; Flickr stores many
photos (`interface-families/asset-library.md`).

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Whiteboard / infinite board (miro Intelligent Canvas; excalidraw Whiteboard; tldraw "very good free whiteboard"; mural visual workspace; whimsical whiteboard for product builders; figjam; milanote organize projects; prior Figma/Miro DOC) | freeform space + tools + (maybe) templates | the artifact is spatial conversation or structure | workshops, diagramming, design jam | live maps or photo editors | Flightradar chrome on Miro hides the board; a marketing hero on Excalidraw hides the canvas that IS the product |
| Raster / vector editor (photopea Free Online Photo Editor + learn; pixlr; sketch-app Design/Collaboration/Prototyping; penpot; prior Canva / Figma) | document + tools + layers/inspector | the artifact is a designed file | image/UI editing | whiteboards or AIS maps | a workshop template gallery on Photopea hides the document; editor toolbars on a live map hide the moving objects |
| Diagram host (lucidchart; diagrams-net / draw.io Security-first diagramming; creately; mermaid-live FlowChart editor; smart-draw tables) | structured graph on a canvas | nodes and edges are the data | architecture / process drawing | photo retouch or flight tracking | an infinite sticky-note board on draw.io hides the diagram model |
| Live spatial instrument (flightradar24 Flight tracker map; flightaware; marinetraffic AIS; openstreetmap; prior windy / earth.nullschool / ventusky) | the map IS the product; nav is layers/coverage | objects move in geography | tracking / live geo | whiteboards or CAD | Miro collaboration chrome on Flightradar24 hides the map; a NASA mission tree on OSM hides the map |
| Chart / math canvas (tradingview Track All Markets; desmos; geogebra; prior observable) | plotted space + instrument chrome | the picture is a function or a market | research / trading / teaching | team whiteboards | a sticky-note canvas on TradingView hides the chart; a broker nav on Desmos hides the graph |
| CAD / 3D (onshape 3D CAD Parts/assemblies/drawings; tinkercad thin; blender-org is a download site) | model + feature tree + view | the artifact is a part or scene | engineering / 3D | photo editors or GIS | Photopea layer chrome on Onshape hides the feature tree. Blender.org proves a product exists; it does not authorize a web CAD UI |

ALTERNATIVES: infinite board, file editor, diagram graph, live map,
plot, feature-tree CAD. Pick from whether objects are freeform,
structured, geographic, or mathematical.

Thin / skip: Invision→Miro, Krita/Inkscape failed, Tinkercad empty
title, Blender download marketing. Count fetch-ok; do not invent
layer panels from blender.org.

## Decision conditions

- **Data shape**: coordinates, layers, selection, scale. If the
  primary object is a row, use a table (`ui/data-display.md`).
- **Collaboration**: boards often share; instruments often watch.
  Presence is optional (`ux/collaboration-concurrency.md`).
- **Platform**: canvases want pointer + keyboard; phones get a
  viewer or a single tool, not a shrunk desktop palette.
- **A11y**: a canvas needs a non-canvas path for the same objects
  (list, table, or structured description). Drag is not a complete
  command channel (`ux/interaction-control.md`, WCAG 2.5.7).
- **RTL**: the artboard may stay LTR (coordinates, time, maps);
  chrome and labels flip. Do not mirror geography.

## Don't

A KPI dashboard around Excalidraw · whiteboard stickies on a
flight map · copying Figma's inspector onto OpenStreetMap ·
inventing multiplayer because Miro has it · one "canvas layout"
for Photopea, TradingView, and Onshape.
