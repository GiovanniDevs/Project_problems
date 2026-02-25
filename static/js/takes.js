const editButtons = document.getElementsByClassName("btn-edit");
const takeText = document.getElementById("id_description");
const takePain = document.getElementById("id_pain_level");
const takeAffected = document.getElementById("id_affected_people");
const takeFrequency = document.getElementById("id_frequency");
const takeForm = document.getElementById("takeForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/*
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated take's ID upon click.
 * - Fetches the content of the corresponding take.
 * - Populates the `takeText` input/textarea with the take's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_take/{takeId}` endpoint.
 */

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let takeId = e.target.getAttribute("data-take_id");
    let takeContent = document.getElementById(`take${takeId}`).innerText;
    let getPain = document.getElementById(`pain${takeId}`).innerText;
    let getFrequency = document.getElementById(`freq${takeId}`).innerText;
    let getAffected = document.getElementById(`affected${takeId}`).innerText;
    takeText.value = takeContent;
    takePain.value = getPain;
    takeFrequency.value = getFrequency;
    takeAffected.value = getAffected;
    submitButton.innerText = "Update";
    takeForm.setAttribute("action", `edit_take/${takeId}`);
  });
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated take's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific take.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let takeId = e.target.getAttribute("data-take_id");
    deleteConfirm.href = `delete_take/${takeId}`;
    deleteModal.show();
  });
}
