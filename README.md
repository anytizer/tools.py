# tools.py
Useful snippets for Python


## Capitalizer:

    cap = CAPITALIZER()
    c = cap.capitalize('id')

## Namifier
    nf = namifier()
    name = "first last"
    raw = nf.namify(name)
    self.assertTrue(raw == "First Last")
    
 Namifier returns [NameDTO](NameDTO.py) with first, middle and last as attributes.
