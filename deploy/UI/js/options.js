// ----- init state -------
const host_name = "http://127.0.0.1:5000";

const listGroupCheckableUpscalesX4 = document.getElementById("listGroupCheckableUpscales1");
const listGroupCheckableUpscalesX8 = document.getElementById("listGroupCheckableUpscales2");
const listGroupCheckableOriginalModel = document.getElementById("listGroupCheckableModels1");
const listGroupCheckableMosaicModel = document.getElementById("listGroupCheckableModels2");
const listGroupCheckablePerceptualLossModel = document.getElementById("listGroupCheckableModels3");
const listGroupCheckableMixLossesModel = document.getElementById("listGroupCheckableModels4");
const loadingSpinner = document.getElementById("loading");

var scale = "SRx4";
var modelName = 'HAT-S_from_scratch';
var ymlFileName = 'HAT-S_SRx4_from_scratch';

// ----- function state -------

function showSpinner(optionId) {
    var loadingSpinner = document.getElementById(optionId);
    loadingSpinner.style.display = 'block';
}

function hideSpinner(optionId) {
    var loadingSpinner = document.getElementById(optionId);
    loadingSpinner.style.display = 'none';
}

function changeModel(spinnerOption) {
    var requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ modelName: modelName }),
    }
    showSpinner(spinnerOption);
    fetch(host_name + '/change_model', requestOptions)
        .then(response => response.json())
        .then(msg => {
            console.log('Response from host:', msg);
            hideSpinner(spinnerOption);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            hideSpinner(spinnerOption);
        });
};

function updateYmlFileName(spinnerOption) {
    ymlFileName = "HAT-S_" + scale + modelName.substring(5);
    console.log("update YAML file name:", ymlFileName);
    changeModel(spinnerOption);
};

function updateScale() {
    var spinnerOption;
    if (listGroupCheckableUpscalesX4.checked) {
        scale = "SRx4";
        spinnerOption = "spinner1"
    } else if (listGroupCheckableUpscalesX8.checked) {
        scale = "SRx8";
        spinnerOption = "spinner2";
    }
    console.log("update upscale option:", scale);
    updateYmlFileName(spinnerOption);
};
listGroupCheckableUpscalesX4.addEventListener('change', updateScale);
listGroupCheckableUpscalesX8.addEventListener('change', updateScale);

function updateModelName() {
    var spinnerOption = "spinner0";
    if (listGroupCheckableOriginalModel.checked) {
        modelName = "HAT-S_from_scratch";
        spinnerOption = "spinner3";
    } else if (listGroupCheckableMosaicModel.checked) {
        modelName = "HAT-S_Patch-Mosaic";
        spinnerOption = "spinner4";
    } else if (listGroupCheckablePerceptualLossModel.checked) {
        modelName = "HAT-S_PerceptualLoss_conv2_2";
        spinnerOption = "spinner5";
    } else if (listGroupCheckableMixLossesModel.checked) {
        modelName = "HAT-S_MixLosses";
        spinnerOption = "spinner6";
    }
    console.log("update model name:", modelName);
    updateYmlFileName(spinnerOption);
};
listGroupCheckableOriginalModel.addEventListener('change', updateModelName);
listGroupCheckableMosaicModel.addEventListener('change', updateModelName);
listGroupCheckablePerceptualLossModel.addEventListener('change', updateModelName);
listGroupCheckableMixLossesModel.addEventListener('change', updateModelName);