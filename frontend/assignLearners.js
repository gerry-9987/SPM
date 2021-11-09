const base_url ="http://ec2-54-205-2-225.compute-1.amazonaws.com"

var staffURL = `${base_url}:5005/staff`;
var courseURL = `${base_url}:5003/course`;
var classURL = `${base_url}:5002/class`;
var takeclassURL = `${base_url}:5007/take_class`;

var app = new Vue({
    el: "#app ",
    data: {
        setClassNo:1,
        courseID: 1,
        // checkedNames:[['Ley Yi', 2]],
        checkedNames:[],
        courses: [],
        classes: [],
        learners: [],
        courseName: "IBM 102",
        class_no: [],
        assigned: 10,
        capacity: 1,
        message: [],
        classes_taken: [],
        already_assigned:[],
        staff: [],
        status: [],
        assigned: 0,
        PostLearners: false
    },
    created: function(){
        this.getNumClasses(),
        this.getClassCapacity(),
        this.getAllClassTaken()
        // this.getLearners()
        // this.assignAllLearners(),
        // this.assignLearners()
    },

    methods: {

        getNumClasses: function() {
            fetch(courseURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data.courses;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            for (var course of result) {
                                if (course.courseID == this.courseID) {
                                    console.log(this.courseID + 1)
                                    for (let i = 1; i < (this.courseID + 2); i++) {
                                        this.class_no.push(i);
                                    }
                                    console.log('class_no')
                                    console.log(this.class_no)
                                }
                            }
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })

        },

        getClassCapacity: function() {
            fetch(classURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data.classes;
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            for (var one_class of result) {
                                if (one_class.courseID == this.courseID && one_class.classID == this.setClassNo) {
                                    this.capacity = one_class.classSize
                                    console.log('capacity')
                                    console.log(this.capacity)
                                }
                            }
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })

        },

        getAllClassTaken: function() {
                console.log('get all classes taken')
                fetch(takeclassURL)
                .then(response => response.json())
                .then(data => {
                    if (data.code === 404) {
                        this.message = data.message;
                    } else {
                        this.classes_taken = data.data.classes_taken;
                        for(var class_taken of this.classes_taken){
                            console.log(this.setClassNo)
                            if (class_taken.classID == this.setClassNo){                                
                                this.already_assigned.push(class_taken.staffID)
                                this.assigned = this.already_assigned.length                     
                            }

                        }
                        console.log('##### Already Assigned:')
                        console.log(this.already_assigned)
                        this.getLearners()
                    }
                })
                .catch(error => {
                    // Errors when calling the service; such as network error,
                    // service offline, etc
                    console.log(this.message + error);
                });
        },

        getLearners: function() {
            console.log('Getting learner details')
            fetch(staffURL)
                .then(response => response.json())
                .then(data => {
                    result = data.data.staff;
                    console.log('Staff')
                    console.log(result);
                    // 3 cases
                    switch (data.code) {
                        case 200:
                            for (var staff of result) {
                                if (staff.department == "Learner") {
                                    if (this.already_assigned.includes(staff.staffID))
                                        this.learners.push([staff.staffName, staff.staffID, '- Already Assigned']);
                                    else{
                                        this.learners.push([staff.staffName, staff.staffID, '- Not Assigned']);
                                    }                    
                                
                                }                               
                            }
                            console.log('Learners!')
                            console.log(this.learners)
                            console.log('Already assigned!')
                            console.log(this.already_assigned)
                            break;
                        case 400:
                        case 500:
                            console.log('failure')
                            break;
                        default:
                            throw `${data.code}: ${data.message}`;
                    }
                })
        },

                
        // if there is more than one learner selected
        // assignAllLearners: function(){
        //     console.log(this.checkedNames)
        //     var numLearners = this.checkedNames.length();
        //     var staffID = "";
        //     for (var i=0; i<numLearners+1; i++) {
        //         staffID = checkedNames[i][0];
        //         console.log(staffID);
        //         this.assignLearners(staffID);
        //     };

        // },

        assignLearners: function() {
            // var temp = this.checkedNames
            // alert(`${temp}`)
            console.log('in assign learners')
            if (this.checkedNames) {

                console.log('Conditions satisfied, post new learners!')
                console.log(this.checkedNames[0][1], this.courseID, this.courseName, this.setClassNo)

                let jsonData = JSON.stringify(
                    {
                        "staffID" : this.checkedNames[0][1],
                        "courseID" : this.courseID,
                        "courseName" : this.courseName,
                        "classID" : this.setClassNo,
                    });

                console.log(jsonData);

                fetch(takeclassURL, {
                        method: "POST",
                        mode: "cors",
                        headers: {
                            "Content-type": "application/json",
                            'Accept': 'application/json'
                        },

                        body: jsonData
                    })
                    .then(response => response.json())
                    .then(data => {
                        console.log(data);
                        result = data.code;
                        console.log(result);
                        // 3 cases
                        switch (result) {
                            case 200:
                                // 201
                                this.assignSuccessful = true;
                                console.log('200 - assigned learners successfully!');
                                alert('Assigned learners successfully!');
                                break;
                            case 300:
                                alert('Learner already assigned!');
                            case 400:
                                // 400
                                this.assignSuccessful = false;
                                break;
                            case 500:
                                // 500
                                console.log(data.message);
                                break;
                            default:
                                throw `${data.code}: ${data.message}`;

                        } // switch
                        this.assignSuccessful = true;
                    })
                    .catch(error => {
                        console.log("Problem in assigning learners" + error);
                    })
            }

            else{
                alert('No learners selected!')
            }
        }





    }

});