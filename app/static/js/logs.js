// $(function () {
//   $("#delete-log").click(function (id) {
//     alert(id);
//   });
// });

// helper funciton
// function getCookie(cname) {
//   var name = cname + "=";
//   var decodedCookie = decodeURIComponent(document.cookie);
//   var ca = decodedCookie.split(";");
//   for (var i = 0; i < ca.length; i++) {
//     var c = ca[i];
//     while (c.charAt(0) == " ") {
//       c = c.substring(1);
//     }
//     if (c.indexOf(name) == 0) {
//       return c.substring(name.length, c.length);
//     }
//   }
//   return "";
// }

async function delete_log(id) {
  if (confirm("Are you sure you want to delete the log")) {
    // const access_token = getCookie("csrftoken");
    // console.log(access_token);
    // console.log(document.cookie);
    const response = await fetch(`/logs/${id}/delete`);
    console.log(response);
    location.reload();
  } else {
    return;
  }
}

// $(function () {
//   $("#filter-platform").keyup(function () {
//     const input = $(this).val();
//     fetch(`/logs/filter/${input}`)
//   });
// });
