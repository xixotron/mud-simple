#vim: set fileencoding=utf-8

rooms = {
    "casa": {
        "description": "Estas en una sucia casa.",
        "exits": {"fuera": "fuera"},
    },
    "fuera": {
        "description": "Estás fuera de una casa. Está lloviendo.",
        "exits": {"dentro": "casa"},
    }
}
