const base_url ="http://ec2-54-205-2-225.compute-1.amazonaws.com"

var course_url = `${base_url}:5003/course`

var app = new Vue({
    el: "#app ",
    computed: {},
    data: {
        course_categories: [
            "IBM",
            "HP",
            "XENON ",
            "Canon",
        ],
        trainers: [
            "Wesley", "Jewel", "Gerry", "HaoYue", "LY"
        ],
        form_course_name: 'Enter course name',
        form_course_category: 0,
        form_number_of_classes: 0,
        form_course_capacity: 0,
        form_course_trainers: [],
        form_required_courses: 'None',
        form_course_details: ''
    },
    methods: {
        submit_new_course: function() {
            console.log('Adding new course')
            console.log(this.form_course_name, this.form_course_category, this.form_number_of_classes, this.form_course_capacity, this.form_course_trainers)

            let jsonData = JSON.stringify({
                courseName: this.form_course_name,
                courseCategory: this.form_course_category,
                courseDetails: this.form_course_details,
                noOfclasses: this.form_number_of_classes,
                prereqCourses: this.form_required_courses,
                noOfClasses: this.form_number_of_classes,
                students: ''
            });

            console.log(course_url)
            fetch(course_url, {
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
                        case 200:
                            console.log('success')
                            alert('Sucessfully created course');
                            break;
                        case 300:
                            alert('Course already exisits! Please change name');
                        case 500:
                            console.log('failure')
                            alert('Failed to create course');
                            break;
                        default:
                            console.log('error')
                            throw `${data.code}: ${data.message}`;
                    }
                })
        }
    }
});