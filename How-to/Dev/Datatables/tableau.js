$(document).ready(function () {
    $('#tab').DataTable({
        language: {
            url: "DataTables/media/French.json"
        },
        dom: "tip",
        pagingType: "simple",
        pageLength: 8,
        order: [[1, 'desc'], [0, 'asc']],
        columns: [
            {type: "text"},
            {type: "html"},
            {orderable: false}
        ]
    });
});