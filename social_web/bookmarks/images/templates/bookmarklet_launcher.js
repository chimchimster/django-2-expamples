(function() {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild(
            document.createElement('script')
        ).src='https://0c87-92-55-176-122.ngrok-free.app/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();