#vim: set fileencoding=utf-8

rooms = {
    "casa": {
        "description": "Estás en una sucia casa.",
        "exits": {"outside": "fuera"},
    },
    "fuera": {
        "description": "Estás fuera de una casa. Está lloviendo.",
        "exits": {"inside": "casa"},
    }
}
