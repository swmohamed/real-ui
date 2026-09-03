# Interface Family: Asset Library / Files / DAM

The primary object is a NAMED FILE or ASSET: stored, found, shared,
permissioned, versioned, or sent. This is not a canvas (the file is
not being painted) and not a docs tree (the object is a blob or
media item, not a topic of prose).

Apply `interface-families/README.md`. This catalog never invents
folder trees, version history, sharing dialogs, or DAM rights
because "file products usually have them."

Label: REAL-WORLD OBSERVATION (SOURCE-OBSERVED 2026-09-03, waves
31 and 36) plus DESIGN PRINCIPLE. Public URLs are mostly marketing
or login shells. They prove the product model. They do not authorize
invented explorer chrome. Play listings prove claimed capabilities
(offline, camera, backup), not in-app layout. OneDrive and iCloud
were thin or UA-blocked this wave — count honesty, not IA.

V7.5 rejected file management for lack of a 20-product corpus.
Wave 31 retained **28/32** fetch-ok production products. That floor
is met. The family still does not become a template.

## Distinct problem space

Users: people who keep, send, or govern files. Jobs: put a thing
somewhere, find it later, give someone access, send a packet, keep
a brand library honest. Frequency is high. Consequence is a leaked
folder, a lost cut, or a wrong brand asset.

WHEN NOT spatial-canvas: Photopea edits pixels; Flickr stores many
photos. WHEN NOT reference-docs: MDN is a topic tree; Drive is a
store of files. WHEN NOT work-queue: Frame.io review is a library
with approval on assets, not a ticket inbox as the home.

## Product families (never average)

| Family | Observed shape | WHY | WHEN | WHEN NOT | TRADEOFF |
|---|---|---|---|---|---|
| Personal / team cloud drive (google-drive "Store and share files"; dropbox store/share/sync; box Intelligent Content; nextcloud Files; sync.com privacy storage; tresorit encrypted exchange; mega / internxt encrypted storage; yandex-disk 360 cloud; egnyte Content Cloud; owncloud share files and folders) | named objects + location + sharing | the job is keep-and-find with permissions | ongoing storage for a person or team | one-shot send, public commons, or a photo editor | Explorer chrome on Smash hides the send; DAM rights language on a family Drive hides simple sharing |
| Send / transfer (fromsmash "Send large files"; mediafire "File storage and sharing made simple") | a packet with an expiry or a download link | the job is get this across once | large one-shot delivery | a durable team drive | Folder trees on a transfer product invent a library the user did not ask to manage. WeTransfer returned an error page this wave — count the product, do not invent a dropzone |
| DAM / brand library (bynder "enterprise DAM"; brandfolder "usable digital asset management"; cloudinary Image and Video Upload / Assets) | governed assets + findability + brand rules | the job is the right file, on-brand, with rights | marketing/creative systems of record | a student's homework folder | Drive-style personal sharing on Bynder hides governance; a CDN optimizer is not a personal photos app |
| Creative review library (frameio File Management / Share & Present / Review & Approvals / Camera to Cloud) | media library + review on the asset | the job is comment and approve the cut | production review | a helpdesk ticket queue or a whiteboard | Ticket inboxes on Frame.io hide the timeline; a Miro board is not a clip library |
| Photo / media library (flickr photographer home; google-photos Edit, Organize, Search, and Backup) | visual library + search/memories | the job is find and relive media | consumer or photographer libraries | enterprise DAM or CAD files | Brand-portal chrome on Flickr hides the photostream; album grids on Egnyte hide compliance |
| Public archive / commons (wikimedia-commons Main Page + Upload file; internet-archive library — JS-required thin) | public catalog of media/texts | the job is deposit or borrow a public object | commons / digital library | private team drives | Personal sharing dialogs on Commons hide community deposit; do not invent Archive.org reader chrome from a JS stub |

ALTERNATIVES: folder explorer, send-link, governed DAM, review library,
photostream, public commons. Pick from whether the object is private,
expiring, brand-governed, under review, or public.

Thin / skip for IA: onedrive UA-block, icloud title-only, pcloud SSL
fail, icedrive 403, smugmug 502, proton-drive timeout, wetransfer
error page, immich thin, kdrive empty title, internet-archive JS stub.
Filestack is an upload API marketing site — supporting vendor, not a
library UI.

## Decision conditions

- **Data shape**: named objects with path, type, size, owner, and
  access. If the primary object is a conversation, use conversation
  space. If it is pixels being edited, use spatial-canvas.
- **Permissions**: view / comment / edit / share / admin are not the
  same. Color-only sharing is not enough
  (`ux/collaboration-concurrency.md`).
- **Task**: keep vs send vs govern vs review vs remember. Those five
  jobs do not share one home.
- **Platform**: desktop wants name+meta density; phone listings claim
  camera, backup, offline (`ux/mobile-states.md`). Do not shrink a
  file tree onto a phone.
- **A11y**: folder trees need keyboard expand/collapse; previews need
  names, not thumbnails only; drag-upload needs a non-drag path
  (WCAG 2.5.7).
- **RTL**: names, extensions, and URLs stay LTR inside RTL chrome.

## Don't

A KPI dashboard as the Drive home · averaging Dropbox, Bynder, Flickr,
and Smash into one "file manager" · inventing version history because
Box named AI · treating Commons as a personal iCloud · copying
Frame.io review onto a family photo backup.
