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
        }
    }
});