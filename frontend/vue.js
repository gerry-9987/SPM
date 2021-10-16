var URL = 'localhost:5003'

// Define a new component called button-counter
Vue.component('nav-bar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: '<nav class="navbar navbar-light bg-light"><div class = "container-fluid" ><a class = "navbar-brand" > Course Management System </a></div ></nav >'
})

var vm = new Vue({
    el: '#nav-bar'
});

var app = new Vue({
    el: "#app ",
    computed: {},
    data: {
        course_categories: [
            "Mechanical Engineer ",
            "Computer Engineer ",
            "Chemical Engineer ",
        ],
        trainers: [
            "Wesley", "Jewel", "Gerry", "HaoYue", "LY"
        ],
        form_course_name: 'Enter course name',
        form_course_category: 0,
        form_number_of_classes: 0,
        form_course_capacity: 0,
        form_course_trainers: []
    },
    methods: {
        submit_new_course: function() {
            console.log('I am clicked')
            console.log(this.form_course_name, this.form_course_category, this.form_number_of_classes, this.form_course_capacity, this.form_course_trainers)

            let jsonData = JSON.stringify({
                form_course_name: this.form_course_name,
                form_course_category: this.form_course_category,
                form_number_of_classes: this.form_number_of_classes,
                form_course_capacity: this.form_course_capacity,
                form_course_trainers: this.form_course_trainers
            });

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