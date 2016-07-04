FILE(REMOVE_RECURSE
  "CMakeFiles/opentld"
  "CMakeFiles/opentld-complete"
  "libopentld/src/opentld-stamp/opentld-install"
  "libopentld/src/opentld-stamp/opentld-mkdir"
  "libopentld/src/opentld-stamp/opentld-download"
  "libopentld/src/opentld-stamp/opentld-update"
  "libopentld/src/opentld-stamp/opentld-patch"
  "libopentld/src/opentld-stamp/opentld-configure"
  "libopentld/src/opentld-stamp/opentld-build"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/opentld.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
