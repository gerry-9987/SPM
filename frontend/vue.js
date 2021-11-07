// Define a new component called button-counter
Vue.component('nav-bar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: ''
})


var vm = new Vue({
    el: '#nav-bar'
});

// Define a new component called button-counter
Vue.component('admin-toolbar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: `<div class="container">
                    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
                        <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                            <svg class="bi me-2" width="40" height="32"></svg>
                            <span class="fs-4">LMS</span>
                        </a>

                        <ul class="nav nav-pills">
                            <li class="nav-item"><a href="index" class="nav-link">Home</a></li>
                            <li class="nav-item"><a href="createCourse" class="nav-link">Course</a></li>
                            <li class="nav-item"><a href="createQuiz" class="nav-link">Quiz</a></li>
                            <li class="nav-item"><a href="assignLearners" class="nav-link">Assign</a></li>
                        </ul>
                    </header>
                </div>`
})


var vm = new Vue({
    el: '#admin-toolbar'
});

// User tool bar
Vue.component('learner-toolbar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: `<div class="container">
                    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
                        <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                            <svg class="bi me-2" width="40" height="32"></svg>
                            <span class="fs-4">LMS</span>
                        </a>

                        <ul class="nav nav-pills">
                            <li class="nav-item"><a href="index" class="nav-link">Home</a></li>
                            <li class="nav-item"><a href="cataloguePage" class="nav-link">Courses</a></li>
                        </ul>
                    </header>
                </div>`
})


var vm = new Vue({
    el: '#learner-toolbar'
});