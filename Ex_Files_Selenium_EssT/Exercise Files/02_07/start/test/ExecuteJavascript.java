import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;

public class ExecuteJavascript {
    public static void main(String[] args) {

        System.setProperty("webdriver.chrome.driver", "/Users/namanapawar/Downloads/chromedriver");

        WebDriver driver = new ChromeDriver();

        driver.get("https://formy-project.herokuapp.com/modal");
        WebElement modelButton=driver.findElement(By.id("modal-button"));
        modelButton.click();
        WebElement modelButton=driver.findElement(By.id("close-button"));
        modelButton.click();



        driver.quit();
    }
}
