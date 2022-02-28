#mkdir -p ~/.streamlit

#echo "[server]

#headless = true

#port = $PORT

#enableCORS = false

#" >~/.streamlit/config.tom1

mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml