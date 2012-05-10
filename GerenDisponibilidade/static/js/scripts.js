function loadCalendar() {
	$(document).ready(function() {

		var date = new Date();
		var d = date.getDate();
		var m = date.getMonth();
		var y = date.getFullYear();

		$('#calendar').fullCalendar({
			header : {
				left : 'prev,next today',
				center : 'title',
				right : 'month,agendaWeek,agendaDay'
			},
			dayNames : ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
			dayNamesShort : ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
			monthNames : ['Janeiro', 'Fevevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agostp', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
			monthNamesShort : ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Aug', 'Set', 'Out', 'Nov', 'Dez'],
			buttonText : {
				prev : '&nbsp;&#9668;&nbsp;', // left triangle
				next : '&nbsp;&#9658;&nbsp;', // right triangle
				prevYear : '&nbsp;&lt;&lt;&nbsp;', // <<
				nextYear : '&nbsp;&gt;&gt;&nbsp;', // >>
				today : 'hoje',
				month : 'mês',
				week : 'semana',
				day : 'dia'
			},
			timeFormat : 'H(:mm)',
			titleFormat : {
				month : "MMMM 'de' yyyy", // September 2009
				week : "d[ yyyy]{ '&#8212;'[ MMM] d 'de' MMMM 'de' yyyy}", // Sep 7 - 13 2009
				day : "dddd, d 'de' MMMM 'de' yyyy"                  // Tuesday, Sep 8, 2009
			},
			editable : false,
			eventClick : function(calEvent, jsEvent, view) {

				alert('Event: ' + calEvent.title);
				alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
				alert('View: ' + view.name);

				// change the border color just for fun
				//$(this).css('border-color', 'red');
				if(calEvent.url) {
					//window.open(event.url);
					//return false;
					alert('opa temos um link aqui');
					return false;
				}

			},
			eventMouseover : function(event, jsEvent, view) {
				$(this).css('border-color', 'red');

			},
			eventMouseout : function(event, jsEvent, view) {
				$(this).css('border-color', '');

			},
			events : [{
				title : 'Evento todo o dia',
				start : new Date(y, m, 1)
			}, {
				title : 'Evento longo',
				start : new Date(y, m, d - 5),
				end : new Date(y, m, d - 2)
			}, {
				id : 999,
				title : 'Evento recorrente',
				start : new Date(y, m, d - 3, 16, 0),
				allDay : false
			}, {
				id : 999,
				title : 'Evento recorrente',
				start : new Date(y, m, d + 4, 16, 0),
				allDay : false
			}, {
				title : 'Reunião',
				start : new Date(y, m, d, 10, 30),
				allDay : false
			}, {
				title : 'Almoço',
				start : new Date(y, m, d, 12, 0),
				end : new Date(y, m, d, 14, 0),
				allDay : false
			}, {
				title : 'Aniversário do Juca',
				start : new Date(y, m, d + 1, 19, 0),
				end : new Date(y, m, d + 1, 22, 30),
				allDay : false
			}, {
				title : 'Compromisso link externo',
				start : new Date(y, m, 28),
				end : new Date(y, m, 29),
				url : 'http://google.com/'
			}]
		});

	});

}

$(function() {
	$(".datapicker").datepicker();
	$('.horas').typeahead({
		source : gerarListaHoras(),
	});
	
	
});

function gerarListaHoras(){
	var horas = new Array();
	for (var i=0; i < 24; i++) {
		for (var j=0; j < 60; j+=30) {
		  var d = new Date(0, 0, 0, i, j, 0, 0);
		  //alert(i+" "+j);
		  		  horas.push(d.toLocaleTimeString());
		  		  
		};
	  
	};
	return horas;
}
