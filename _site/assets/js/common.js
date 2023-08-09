$(document).ready(function () {
    $('a.abstract').click(function () {
        $(this).parent().parent().find(".abstract.hidden").toggleClass('open');
    });
    $('a.bibtex').click(function () {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
    });
    $('a.pmid').click(function () {
        $(this).parent().parent().find(".pmid.hidden").toggleClass('open');
    });

    $('a.doi').click(function () {
        $(this).parent().parent().find(".doi.hidden").toggleClass('open');
    });
    $('a.pmcid').click(function () {
        $(this).parent().parent().find(".pmcid.hidden").toggleClass('open');
    });
    $('.navbar-nav').find('a').removeClass('waves-effect waves-light');
});
