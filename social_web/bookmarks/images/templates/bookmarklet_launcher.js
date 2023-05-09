(function() {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet();
    } else {
        document.body.appendChild(
            document.createElement('script')
        ).src='https://b36e-92-55-176-6.ngrok-free.appp/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();