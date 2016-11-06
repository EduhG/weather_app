$(".form_datetime").datetimepicker({
    format: "yyyy-mm-dd",
    autoclose: true,
    pickTime: false,
    todayBtn: true,
    disabledHours:true,
    useCurrent:true
});

window.onload = function () {
    /*************************************************************************
     * Total Reported Cases Chart
    *************************************************************************/
    $.ajax({
        url : 'json_temps',
        dataType : 'json',
        type : 'GET',
        success: function(data){
            var dates = [];
            var temps = [];

            for(var i in data) {
                dates.push(data[i].date_time);
                temps.push(data[i].temp);
            }

            var config = {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [{
                        label: "Monthly Temperature Reading",
                        data: temps,
                        fill: true,
                        borderColor: "#4bc0c0"
                }]
                },
                options: {
                    scales: {
                        xAxes: [{
                            gridLines: {
                                display: false
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Last 10 Days'
                            }
                        }],
                        yAxes: [{
                            scaleLabel: {
                                display: true,
                                labelString: 'Temperature Readings'
                            }
                        }]
                    },
                    legend: {
                        display: false
                    },
                    tooltips: {
                        callbacks: {
                            label: function (tooltipItem) {
                                return tooltipItem.yLabel;
                            }
                        }
                    }
                }
            };

            var ctx = document.getElementById("chartContainer").getContext("2d");
            new Chart(ctx, config);
        },
        error: function( jqXhr, textStatus, errorThrown ){
            console.log( errorThrown );
        }
    });
}
