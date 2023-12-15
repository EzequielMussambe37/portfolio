function onDataFromPython(event) {
    //console.log("this is the event")
    console.log(event)

    const data = event.detail;
    var spec;
    spec = data.args.spec["data"];

    container = document.getElementById('accordion');
    const card = document.createElement('div');

    if (container.innerHTML == "") {
        for (title of Object.keys(spec)) {
            project = spec[title]

            console.log("dataset the original")
            console.log(project[0].url)
                //JSON.parse(spec[title])
            card.classList = 'card-body';
            var color = "white"
            const content =
                `
    <div class="card">
        <a class="card-href"  href="${project[0].url}" target="_blank">  
            <img class="card-img" src="${project[0]['image_url']}" alt="" width=200/>
        </a>
        <div class="container">
            <h3>
            <b>${title}</b>
            </h3>
            <p style="text-overflow: ellipsis; color:blue">${project[0].description}</p><br>

        </div>
    </div>

    `;
            container.innerHTML += content;
        }
    }
    Streamlit.setFrameHeight(document.documentElement.clientHeight);
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onDataFromPython);
Streamlit.setComponentReady();

{ /* <i id="${title}"class="fa fa-heart fa-lg" style="color:${color};size:20px;"></i> */ }