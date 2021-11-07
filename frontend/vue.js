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

// Define a new component called button-counter
Vue.component('admin-toolbar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: `<div class="container-fluid section-wrapper">
                    <h2>Tools for Administrators</h2>
                    <div class="border border-grey rounded">
                        <div class="row m-4">
                            <!-- tool 1-->
                            <div class="col-md-3">
                                <div class="card">
                                    <img src="../images/Rectangle 13.jpg" class="card-img-top" alt="..." />
                                    <div class="card-body">
                                        <p class="card-text text-center "><a href="createCourse">Create Course</a></p>
                                    </div>
                                </div>
                            </div>
                            <!-- tool 2-->
                            <div class="col-md-3">
                                <div class="card">
                                    <img src="../images/Rectangle 13.jpg" class="card-img-top" alt="..." />
                                    <div class="card-body">
                                        <p class="card-text text-center"><a href="manageCourse">Manage Course</a></p>
                                    </div>
                                </div>
                            </div>
                            <!-- end of tools-->
                            <!-- tool 3-->
                            <div class="col-md-3">
                                <div class="card">
                                    <img src="../images/Rectangle 13.jpg" class="card-img-top" alt="...">
                                    <div class="card-body">
                                    <p class="card-text text-center"><a href="assignLearners">Assign Learners</a></p>
                                    </div>
                                </div>
                            </div>
                            <!-- end of tools-->
                        </div>
                    </div>
                </div>`
})


var vm = new Vue({
    el: '#admin-toolbar'
});

// User tool bar
Vue.component('admin-toolbar', {
    data: function() {
        return {
            count: 0
        }
    },
    template: `<div class="container-fluid section-wrapper">
                    <h2>Tools for Administrators</h2>
                    <div class="border border-grey rounded">
                        <div class="row m-4">
                            <!-- tool 1-->
                            <div class="col-md-3">
                                <div class="card">
                                    <img src="../images/Rectangle 13.jpg" class="card-img-top" alt="..." />
                                    <div class="card-body">
                                        <p class="card-text text-center "><a href="cataloguePage">cataloguePage</a></p>
                                    </div>
                                </div>
                            </div>
                            <!-- end of tools-->
                        </div>
                    </div>
                </div>`
})


var vm = new Vue({
    el: '#admin-toolbar'
});