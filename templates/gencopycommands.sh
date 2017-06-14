locate epub.css | puf '["sudo cp epub.css " +x for x in lines if "workspace" not in str(x)]'
echo
locate default.latex | puf '["sudo cp default.latex " +x for x in lines  if "workspace" not in str(x)]'
