using PlayFab;
using PlayFab.ClientModels;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

// This is used with a known DB and API known as PlayFab. Great and secure for startups!

public class AccountManager : MonoBehaviour
{
    private string userName;
    private string userEmail;
    private string userPassword;

    //public InputField username;
    public InputField e_mail;
    public InputField password;
    public InputField confirmPassword;
    public Text errorText;
    public Button loginButton;
    public Button registerButton;

    public GameObject loadingScreen;

    public void GetUserEmail(string email)
    {
        userEmail = email;
    }

    public void GetUserPass(string pass)
    {
        userPassword = pass;
    }

    public void GetUserName(string name)
    {
        userName = name;
    }

    #region Login
    public void Start()
    {
        //Note: Setting title Id here can be skipped if you have set the value in Editor Extensions already.
        if (string.IsNullOrEmpty(PlayFabSettings.TitleId))
        {
            Debug.Log("PlayFabSettings TitleId was empty. Fixing now!");
            PlayFabSettings.TitleId = "6E16C"; // Please change this value to your own titleId from PlayFab Game Manager
        }
        e_mail.text = PlayerPrefs.GetString("Username", e_mail.text);
    }

    private void OnLoginSuccess(LoginResult result)
    {
        Debug.Log("Congratulations, you made a successful API call!");
        PlayerPrefs.SetString("Username", e_mail.text);
        loadingScreen.SetActive(true);
        SceneManager.LoadSceneAsync("MainMenu", LoadSceneMode.Single);
    }

    private void OnLoginFailure(PlayFabError error)
    {
        Debug.LogError("Here's some debug information:");
        Debug.LogError(error.GenerateErrorReport());
        errorText.color = Color.red;
        errorText.text = "Failed to login because: " + error.GenerateErrorReport();
        loginButton.interactable = true;
    }

    public void Login()
    {
        var lRequest = new LoginWithEmailAddressRequest { Email = userEmail, Password = userPassword };
        PlayFabClientAPI.LoginWithEmailAddress(lRequest, OnLoginSuccess, OnLoginFailure);
        Color orange = new Color(0.9921569f, 0.4196079f, 0.0509804f);
        errorText.color = orange;
        errorText.text = "Logging in...";
        loginButton.interactable = false;
    }


    #endregion

    #region Register

    private void OnRegisterSuccess(RegisterPlayFabUserResult result)
    {
        Debug.Log("Congratulations, you made your account!");
        errorText.color = Color.green;
        errorText.text = "You're registered! Now, try logging in.";
    }

    private void OnRegisterFailure(PlayFabError error)
    {
        Debug.LogError("Here's some debug information:");
        Debug.LogError(error.GenerateErrorReport());
        errorText.color = Color.red;
        errorText.text = "Failed to register because: " + error.GenerateErrorReport();
        registerButton.interactable = true;
    }

    public void Register()
    {
        if (confirmPassword.text != password.text)
        {
            errorText.color = Color.red;
            errorText.text = "Failed to register because: Your confirm password doesn't match with your password!";
            Debug.Log("Your confirm password doesn't match with your password!");
            return;
        }
        else
        {
            RegisterNow();
            registerButton.interactable = false;
        }
    }

    private void RegisterNow()
    {
        var rRequest = new RegisterPlayFabUserRequest { Username = userName, Email = userEmail, Password = userPassword };
        PlayFabClientAPI.RegisterPlayFabUser(rRequest, OnRegisterSuccess, OnRegisterFailure);
        Color orange = new Color(0.9921569f, 0.4196079f, 0.0509804f);
        errorText.color = orange;
        errorText.text = "Registering...";
    }

    #endregion

    #region Logout

    public void Logout()
    {
        if (PlayFabClientAPI.IsClientLoggedIn())
        {
            Color orange = new Color(0.9921569f, 0.4196079f, 0.0509804f);
            errorText.color = orange;
            errorText.text = "You can't signout. Just close the game to do so.";
        }
    }

    #endregion

    #region Recovery

    private void OnSendRecoveryEmailSuccess(SendAccountRecoveryEmailResult result)
    {
        Debug.Log("Congratulations, Your recovery email has been sent!");
        errorText.color = Color.green;
        errorText.text = "Your recovery email has been sent! Check your inbox to find the email.";
    }

    private void OnSendRecoveryEmailFailure(PlayFabError error)
    {
        Debug.LogError("Here's some debug information:");
        Debug.LogError(error.GenerateErrorReport());
        errorText.color = Color.red;
        errorText.text = "Failed to send recovery email because: " + error.GenerateErrorReport();
    }

    public void SendRecoveryEmail()
    {
        Color orange = new Color(0.9921569f, 0.4196079f, 0.0509804f);
        errorText.color = orange;
        errorText.text = "Currently, the API for the account recovery is not properly setup. You will have to contact the developer with the same email as the account you are trying to recover. Email: teamdevil101@gmail.com";

        var ripRequest = new SendAccountRecoveryEmailRequest { Email = userEmail, TitleId = "6E16C" };
        PlayFabClientAPI.SendAccountRecoveryEmail(ripRequest, OnSendRecoveryEmailSuccess, OnSendRecoveryEmailFailure);
        errorText.color = orange;
        errorText.text = "Sending recovery email...";
    }
    
    #endregion

}

