#vim: set fileencoding=utf-8

rooms = {
    "casa": {
        "descripcion": "Estas en una sucia casa.",
        "salidas": {"fuera"},
    },
    "fuera": {
        "descripcion": "Estás fuera de una casa. Está lloviendo.",
        "salidas": {"dentro": "casa"},
    }
}
