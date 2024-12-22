#vim: set fileencoding=utf-8

rooms = {
    "Casa": {
        "description": "Estás en una sucia casa.",
        "exits": {"outside": "Fuera"},
    },
    "Fuera": {
        "description": "Estás fuera de una casa. Está lloviendo.",
        "exits": {"inside": "Casa"},
    }
}
