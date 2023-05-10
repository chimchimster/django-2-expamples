(function() {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild(
            document.createElement('script')
        ).src='https://9241-87-255-208-226.ngrok-free.app/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();