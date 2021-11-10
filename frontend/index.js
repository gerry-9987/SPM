var app = new Vue({
    el: "#app ",
    data: {
        showWelcomeMessage: true,
        showLearnerTools: false,
        showAdminTools: false

    },
    created: function() {},
    computed: {},
    methods: {
        showLearner: function() {
            this.showWelcomeMessage = false;
            this.showLearnerTools = true
        },
        showAdmin: function() {
            this.showWelcomeMessage = false;
            this.showAdminTools = true
        }
    },
});