MagickPillow is a really basic library which only converts between Pillow and Wand objects. All operations are performed in memory, but it could be further optimized -- it currently imports/exports files in PNG format, and the encoding/decoding is wasting time.
