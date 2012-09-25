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
			monthNames : ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
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
				this.insertDefaultDateFimFrequencia();
				return;
			}
			if ($('div#frequencia input#id_frequencia_1').is(":checked")) {
				$('div#div_id_dataFimFrequencia').hide('slow');
				this.insertDefaultDateFimFrequencia();
			} else {
				$('div#div_id_dataFimFrequencia').show('slow');
				this.removeDefaultDateFimFrequencia();
			}

			if ($('div#frequencia input#id_frequencia_3').is(":checked")) {
				$('div#div_id_diaSemana').show('slow');
			} else {
				$('div#div_id_diaSemana').hide('slow');
			}
		},
		insertDefaultDateFimFrequencia: function(){
			$('input#id_dataFimFrequencia').val('01/01/1900');
		},
		removeDefaultDateFimFrequencia: function(){
			if($('input#id_dataFimFrequencia').val() == '01/01/1900'){
				$('input#id_dataFimFrequencia').val('');
			}
		}
						
		
	}
	Frequencia.atualizar();

	$('div#frequencia').change(function() {
		Frequencia.atualizar();
	})
	
	
	
	
	$('div#disponibilidade-aula table tbody th.celula-disponibilidade').click(function() {
		console.log($(this).attr('dia')+' '+$(this).attr('hora'));
		
		$.ajax({
            async: true,
            url: '/professor/disponibilidadeAula',
            data: { dia: $(this).attr('dia'), hora: $(this).attr('hora') },
            context: this,
            success: function(data) {
                console.log('success: '+data.result);
                DisponibilidadeAula.seletorCelula = $(this);
                if(data.result == 'added'){
                	DisponibilidadeAula.marcarSelecionado();
                }else if(data.result == 'removed'){
                	DisponibilidadeAula.marcarNaoSelecionado();
                }
                
            },
            error : function(){
            	console.log('Erro ao salvar disponibilidade');
            }
        });
		
	});
	
	
	
	
});

var DisponibilidadeAula = {
	
		dia: '',
		hora: '',	
		seletorCelula : '',
	
		marcarSelecionado: function(){
			this.seletorCelula.removeClass('nao-selecionado');
			this.seletorCelula.addClass('selecionado');
		},
		marcarNaoSelecionado: function(){
			this.seletorCelula.removeClass('selecionado');
			this.seletorCelula.addClass('nao-selecionado');
		},
		
		carregarDadosDoServidor: function(){
			$.ajax({
	            async: true,
	            url: '/professor/getDisponibilidadeAula',
	            context: this,
	            success: function(data) {
	                console.log('success: '+data);
	                
	                $('div#disponibilidade-aula table tbody th.celula-disponibilidade').each(function() {
	                	var seletor = $(this);
	                	$.each(data, function(i, item) {
						    if(seletor.attr('dia') == item.dia && seletor.attr('hora') == item.hora){
						    	console.log('Selecionado: '+item.dia+' '+item.hora);
						    	DisponibilidadeAula.seletorCelula = seletor;
						    	DisponibilidadeAula.marcarSelecionado();
					    	}
						});
					    
					});
	                
	            },
	            error : function(){
	            	console.log('Erro ao salvar disponibilidade');
	            }
        	});
		
		}
	
	}
	
	$(function() {
		DisponibilidadeAula.carregarDadosDoServidor();
	});



/* Default class modification */
$.extend( $.fn.dataTableExt.oStdClasses, {
	"sWrapper": "dataTables_wrapper form-inline"
} );

/* API method to get paging information */
$.fn.dataTableExt.oApi.fnPagingInfo = function ( oSettings )
{
	return {
		"iStart":         oSettings._iDisplayStart,
		"iEnd":           oSettings.fnDisplayEnd(),
		"iLength":        oSettings._iDisplayLength,
		"iTotal":         oSettings.fnRecordsTotal(),
		"iFilteredTotal": oSettings.fnRecordsDisplay(),
		"iPage":          Math.ceil( oSettings._iDisplayStart / oSettings._iDisplayLength ),
		"iTotalPages":    Math.ceil( oSettings.fnRecordsDisplay() / oSettings._iDisplayLength )
	};
}

/* Bootstrap style pagination control */
$.extend( $.fn.dataTableExt.oPagination, {
	"bootstrap": {
		"fnInit": function( oSettings, nPaging, fnDraw ) {
			var oLang = oSettings.oLanguage.oPaginate;
			var fnClickHandler = function ( e ) {
				e.preventDefault();
				if ( oSettings.oApi._fnPageChange(oSettings, e.data.action) ) {
					fnDraw( oSettings );
				}
			};

			$(nPaging).addClass('pagination').append(
				'<ul>'+
					'<li class="prev disabled"><a href="#">&larr; '+oLang.sPrevious+'</a></li>'+
					'<li class="next disabled"><a href="#">'+oLang.sNext+' &rarr; </a></li>'+
				'</ul>'
			);
			var els = $('a', nPaging);
			$(els[0]).bind( 'click.DT', { action: "previous" }, fnClickHandler );
			$(els[1]).bind( 'click.DT', { action: "next" }, fnClickHandler );
		},

		"fnUpdate": function ( oSettings, fnDraw ) {
			var iListLength = 5;
			var oPaging = oSettings.oInstance.fnPagingInfo();
			var an = oSettings.aanFeatures.p;
			var i, j, sClass, iStart, iEnd, iHalf=Math.floor(iListLength/2);

			if ( oPaging.iTotalPages < iListLength) {
				iStart = 1;
				iEnd = oPaging.iTotalPages;
			}
			else if ( oPaging.iPage <= iHalf ) {
				iStart = 1;
				iEnd = iListLength;
			} else if ( oPaging.iPage >= (oPaging.iTotalPages-iHalf) ) {
				iStart = oPaging.iTotalPages - iListLength + 1;
				iEnd = oPaging.iTotalPages;
			} else {
				iStart = oPaging.iPage - iHalf + 1;
				iEnd = iStart + iListLength - 1;
			}

			for ( i=0, iLen=an.length ; i<iLen ; i++ ) {
				// Remove the middle elements
				$('li:gt(0)', an[i]).filter(':not(:last)').remove();

				// Add the new list items and their event handlers
				for ( j=iStart ; j<=iEnd ; j++ ) {
					sClass = (j==oPaging.iPage+1) ? 'class="active"' : '';
					$('<li '+sClass+'><a href="#">'+j+'</a></li>')
						.insertBefore( $('li:last', an[i])[0] )
						.bind('click', function (e) {
							e.preventDefault();
							oSettings._iDisplayStart = (parseInt($('a', this).text(),10)-1) * oPaging.iLength;
							fnDraw( oSettings );
						} );
				}

				// Add / remove disabled classes from the static elements
				if ( oPaging.iPage === 0 ) {
					$('li:first', an[i]).addClass('disabled');
				} else {
					$('li:first', an[i]).removeClass('disabled');
				}

				if ( oPaging.iPage === oPaging.iTotalPages-1 || oPaging.iTotalPages === 0 ) {
					$('li:last', an[i]).addClass('disabled');
				} else {
					$('li:last', an[i]).removeClass('disabled');
				}
			}
		}
	}
} );

jQuery.extend( jQuery.fn.dataTableExt.oSort, {
    "alt-string-pre": function ( a ) {
   		valor = $(a).attr('valor');
   		console.log(valor);
        return valor;
    },
     
    "alt-string-asc": function( a, b ) {
        return ((a < b) ? -1 : ((a > b) ? 1 : 0));
    },
 
    "alt-string-desc": function(a,b) {
        return ((a < b) ? 1 : ((a > b) ? -1 : 0));
    }
} );





function StarRating(selector){

	this.selector = selector;

	this.loadData = function(){
		$.ajax({
	            async: false,
	            url: '/professor/getInteressesDisciplina',
	            type: "GET",
	            context: this,
	            success: function(data) {
	            var selector = this.selector;
	                $.each(data,function(i, item){
	                	console.log('carregando interesse de disciplina: '+item.idDisciplina+' Nota:'+item.nivel);
	                	$.each(selector, function(){
	                		//console.log($(this).attr('idDisciplina'))
	                		if($(this).attr('idDisciplina') == item.idDisciplina){
	                			starR= new StarRatingRow($(this).find('div.rating'));
	                			starR.changeValue(item.nivel);
	                		}
	                	});
	                });
	                
	            },
	            error : function(){
	            	console.log('Erro ao carregar interesse de disciplina');
	            },
	            complete: function() {
	            
	            }
        });
	}
}
jQuery.exists = function(selector) {return ($(selector).length > 0);}

$(document).ready(function() {
	if ($.exists("#tabela-disciplinas-preferencia")) { 
		console.log('Carregando dados de disciplinas de preferencia');
		var starRating = new StarRating($('#tabela-disciplinas-preferencia tbody tr'));
		starRating.loadData();
	}
})



var oTable = null;
/* Table initialisation */
$(document).ready(function() {
	oTable = $('#tabela-disciplinas-preferencia').dataTable( {
		//"sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
		"sPaginationType": "bootstrap",
		"oLanguage": {
        "sZeroRecords": "Não há resultados",
        "sInfoEmpty": "Mostrando 0 de 0 disciplinas no total de 0",
        "sInfo": "Mostrando _START_ de _END_ disciplinas no total de  _TOTAL_",
        "sInfoFiltered": "(filtrando de _MAX_ disciplinas)",
        "oPaginate": {
        "sFirst": "Primeira",
        "sLast": "Última",
        "sNext": "Próxima",
        "sPrevious": "Anterior"},
        "sSearch": "Filtrar:",
        "sLengthMenu": "_MENU_ disciplinas por página",
        
    	},
    	"bAutoWidth": false,
    	"aoColumns": [
			null,
			null,
			{ "sType": "alt-string","sWidth":"150px" },
		]
	} );
});

function StarRatingRow(selector){
	
	this.$selector = selector,
	this.value = 0;

	this.changeValue = function(value){
		this.value = value;
		if(this.$selector.attr('valor') == value){
			console.log('clicou no mesmo valor! limpar!');
			this.clearRating();
			return;
		}
		this.$selector.attr('valor',value);
		//this.changeValueServer(this.$selector.parent().parent().attr('idDisciplina'), value)
		this.$selector.find('span').each(function(){
			if(value >= $(this).attr('valor')){
				$(this).addClass('selecionado');
			}else{
				$(this).removeClass('selecionado');
			}
		});
	},
	
	this.clearRating = function(){
		this.$selector.attr('valor',0);
		this.value = 0;
		//this.changeValueServer(this.$selector.parent().parent().attr('idDisciplina'), 0)
		this.$selector.find('span').each(function(){
			if($(this).hasClass('selecionado') == true){
				$(this).removeClass('selecionado');
			}
		});
	},
	
	this.getValue = function(){
		return this.value;
	},
	
	this.changeValueServer= function(idDisciplina, value){
		$.ajax({
	            async: false,
	            url: '/professor/informarInteresseDisciplina',
	            type: "GET",
	            data: { nivel: value, idDisciplina: idDisciplina },
	            success: function(data) {
	                //console.log('interesse de disciplina: '+data);
	            },
	            error : function(){
	            	console.log('Erro ao salvar interesse de disciplina');
	            }
        	});
        this.changeValue(value);
	}
}





$(document).ready(function() {

	$('div.rating span').click(function(){
		starR= new StarRatingRow($(this).parent());
		if( $(this).parent().attr('valor') == $(this).attr('valor') && $(this).hasClass('selecionado')){
			starR.changeValueServer($(this).parent().parent().parent().attr('idDisciplina'), 0);
		}else{
			starR.changeValueServer($(this).parent().parent().parent().attr('idDisciplina'), $(this).attr('valor'));
		}
		//starR.changeValue($(this).attr('valor'));
		
		
		//atualiza valor no oTable
		aPos = oTable.fnGetPosition( $(this).parent().parent().get(0) );
		aData = oTable.fnGetData( aPos[0] );
		aData[3] = $(aData[3]).attr('valor', starR.getValue());
		//console.log(aData[3]);
		 
	});

});