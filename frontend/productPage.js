// Accordion
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

var app = new Vue({
    el: "#app ",
    computed: {},
    data: {
        courseTrainer: 'Somebody',
        courseSize: 100,
        coursePrequisites: [],
        courseGradingBreakdown: 'Like that lorh',
        courseClasses: "I'm not sure about this yet",
        courseChapters: 0
    },
    methods: {
        getCourseDetails: function() {
            console.log('I am clicked')
            fetch(`${'URL'}`, {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json"
                    },
                    body: jsonData
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                    result = data.data;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 201:
                            console.log('success')
                                // Upack the JSON object returned and assign to variables
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        }
    }
});