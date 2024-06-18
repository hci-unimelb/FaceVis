**getOverlays**
Display a list containing the names of all texture names for a specific Overlay category
*Arguments*:
*CAT*: the name of the overlay category

*Return value*: JSON-list of strings

*Example*: `getOverlays {"CAT":"tattos"}`

**setOverlay**
Set the texture of an overlay category to a given value with a given color.
A value for alpha can be set, which specifies the opacity of the texture.
*Arguments*:
*CAT*: the name of the overlay category
*VAL*: the name of the texture to be set
*COLOR*: value/name of the color to be set, this value can be hexadecimal (rgb:"#ffffff"/rgba:"#ffffffff") or a color name ("red").

*Return value*: none

*Example*: `setOverlay {"CAT":"tattoos","VAL":"viking","COLOR":"#123456FF"}`

**getCharacters**
Display a list containing the names of all the saved and available characters.
*Arguments*: none

*Return value*: JSON-list of strings

*Example*: getCharacters

**setCharacter**
Load a given character preset
*Arguments*:
*NAME*: the name of the desired character preset. Optionally can be prefixed with "packNameString/"

*Return value*: JSON-object containing the fields in the examples. In case of an error occuring, only "ERROR" field will be returned.

*Example*: setCharacter {"NAME":"Brooklyn"}
*Example*: setCharacter {"NAME":"PartyPack/Brooklyn"}
->```
{
    "MODEL":"adult",
    "SKIN":"realistic",
    "ERROR":false,
    "PACK":"PartyPack",
    "MASK":"adult",
    "NAME":"Brooklyn",
}```

**setSkinColor**
Set the color of the skin texture to a given value
*Arguments*:
*COLOR*: value/name of the color to be set, this value can be hexadecimal (rgb:"#ffffff"/rgba:"#ffffffff") or a color name ("red")

*Return value*: none

*Example*: setSkinColor {"COLOR":"#003300FF"}

***
**getAvailableOverlays**

Gets all the overlay textures for the selected overlay category

*Arguments*: a category name: { "CAT": categoryNameString }

*Return value*: list of strings representing available overlays names in requested category
***

***
**getAvailableOverlayCategories**

Gets all the available overlay categories for the current model

*Arguments*: none

*Return value*: list of strings representing available overlays categories
***

*Example*: `setOverlay {"CAT":"tattoos","VAL":"viking","COLOR":"#123456FF"}`