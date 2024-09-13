for file in *; do
    if [[ -f $file && $file != .py && $file != "README.md" ]];then
        mv "$file" "$file.py"
    fi
done