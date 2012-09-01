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
			allDayText : 'Dia Inteiro',
			timeFormat : {
				agenda : 'H:mm{ - H:mm}'
			},
			timeFormat : 'H:mm{ - H:mm}',
			axisFormat : 'H:mm',
			titleFormat : {
				month : "MMMM 'de' yyyy", // September 2009
				week : "d[ yyyy]{ '&#8212;'[ MMM] d 'de' MMMM 'de' yyyy}", // Sep 7 - 13 2009
				day : "dddd, d 'de' MMMM 'de' yyyy" // Tuesday, Sep 8, 2009
			},
			editable : false,
			eventClick : function(calEvent, jsEvent, view) {

				//alert('Event: ' + calEvent.title);
				//alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
				//alert('View: ' + view.name);

				// change the border color just for fun
				//$(this).css('border-color', 'red');
				if (calEvent.url) {
					//window.open(event.url);
					//return false;
					//alert('opa temos um link aqui');
					//return false;
				}

			},
			eventMouseover : function(event, jsEvent, view) {
				$(this).css('border-color', 'red');

			},
			eventMouseout : function(event, jsEvent, view) {
				$(this).css('border-color', '');

			},
			events : {
				url : '/professor/get-compromissos',
				type : 'GET',
				//data: {
				//   custom_param1: 'something',
				//   custom_param2: 'somethingelse'
				//},
				error : function() {
					alert('there was an error while fetching events!');
				},
				//color : 'yellow', // a non-ajax option
				//textColor : 'black' // a non-ajax option
			},
			loading : function(bool) {
				if (bool)
					$('.loading').show();
				else
					$('.loading').hide();
			}
		});

	});

}

$(function() {
	$(".datapicker").datepicker();
	$('.horas').typeahead({
		source : gerarListaHoras(),
	});

});

function gerarListaHoras() {
	var horas = new Array();
	for (var i = 0; i < 24; i++) {
		for (var j = 0; j < 60; j += 30) {
			var d = new Date(0, 0, 0, i, j, 0, 0);
			//alert(i+" "+j);
			horas.push(d.toLocaleTimeString());

		};

	};
	return horas;
}

$(function() {
	if ($('input#diaInteiro').is(":checked")) {
		$('div#div_id_horaFim, div#div_id_horaInicio').hide('slow');
		$('input#id_horaInicio,input#id_horaFim').val('');
	}

	$('input#diaInteiro').click(function() {
		if ($(this).is(":checked")) {
			$('div#div_id_horaFim, div#div_id_horaInicio').hide('slow');
			$('input#id_horaInicio,input#id_horaFim').val('');
			//alert('esconder');
		} else {
			$('div#div_id_horaFim, div#div_id_horaInicio').show('slow');
			//alert('mostrar');
		}

	});

	//recorrencia
	var Frequencia = {
		atualizar : function() {
			if ($('div#frequencia input').is(":checked") == false) {
				$('div#div_id_dataFimFrequencia').hide('slow');
				$('div#div_id_diaSemana').hide('slow');
				return;
			}
			if ($('div#frequencia input#id_frequencia_1').is(":checked")) {
				$('div#div_id_dataFimFrequencia').hide('slow');
			} else {
				$('div#div_id_dataFimFrequencia').show('slow');
			}

			if ($('div#frequencia input#id_frequencia_3').is(":checked")) {
				$('div#div_id_diaSemana').show('slow');
			} else {
				$('div#div_id_diaSemana').hide('slow');
			}

		}
	}
	Frequencia.atualizar();

	$('div#frequencia').change(function() {
		Frequencia.atualizar();
	})
});

