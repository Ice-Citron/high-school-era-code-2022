# BakeSell and Early Programming Projects

This repository contains an archive of the projects I started from 2019 to 2022, 
during middle school. The repository also contains later coding practices I did 
from my early middle-school study sessions.

I spent more than 200 hours on BakeSell, an unfinished Python/Tkinter app
for Mrs. Tapp's bake-sale management. It includes Google API integration.
I also designed the interface in Adobe Illustrator.

![BakeSell dashboard design][dashboard]

*An original Illustrator design for the BakeSell dashboard.*

[App source](bake_sell/) · [Interface designs][designs]

## Why I built BakeSell

For my Duke of Edinburgh Bronze Award, I wanted to make an app that could help 
Mrs. Tapp manage bake-sale events. The app would track customer orders and the 
products still available for sale.

I put substantial time into both the interface and the Python code.
Although I did not finish the app, this work matters to me.
It records my attempt to build a complete tool for another person.

## What the code includes

The source contains code for these workflows:

- Create events and change their names or dates.
- Define products and prices for each event.
- Record products made and sold, with updates to available stock.
- Record costs and time spent.
- Calculate revenue and profit, with charts and tables.
- Create Google Forms and retrieve submitted responses.
- Save and retrieve JSON data through Google Drive.
- Record actions for undo and redo.

## Interface design

I designed the app screens in Adobe Illustrator.
The repository includes the editable document and exported SVG artboards.
The Tkinter interface uses separate image assets in the `GUI/` folders.

- [Original Illustrator document][illustrator]
- [Exported artboards][exports]
- [Design assets][assets]

## Repository structure

```text
.
├── bake_sell/
│   ├── Main.py                    # Main Tkinter interface
│   ├── App-main.py                # Development script
│   ├── functions.py               # App data and business logic
│   ├── forms.py                   # Google authentication and Forms code
│   ├── undo.py                    # Action history and undo/redo code
│   ├── default.py                 # Initial data structure
│   ├── data.json                  # Retained app data
│   ├── undo.json                  # Retained action-history data
│   ├── GUI/                       # Individual screens and image assets
│   ├── adobe-illustrator-designs/  # Original interface design files
│   ├── Cloud base resource/       # Google Drive experiments
│   ├── Google form resource/      # Google Forms experiments
│   └── Junk file of projects/     # Earlier tests and development files
├── programming-practice/
│   ├── java/
│   ├── sql/
│   └── google-kickstart/
├── LICENSE
└── README.md
```

## Project status

Development stopped before I completed the app.
The interface and feature scope became difficult for me to manage.

This is a historical snapshot. It has no verified installation procedure.
The code contains local paths and depends on Google authentication.
A fresh setup needs a separate review of dependencies and configuration.

## Other early exercises

- [Java](programming-practice/java/) — Language tutorials and data structures.
- [SQL](programming-practice/sql/) — Database queries and schema exercises.
- [Google Kick Start](programming-practice/google-kickstart/) — Python attempts.

Some of these exercises date from 2023.

## Licence

See [LICENSE](LICENSE) for the MIT licence.
Retain the original attribution for third-party icons and other assets.

[dashboard]: <bake_sell/adobe-illustrator-designs/exports/Artboard 1.svg>
[designs]: bake_sell/adobe-illustrator-designs/
[illustrator]: bake_sell/adobe-illustrator-designs/bakesale-dashboard.ai
[exports]: bake_sell/adobe-illustrator-designs/exports/
[assets]: bake_sell/adobe-illustrator-designs/assets/
