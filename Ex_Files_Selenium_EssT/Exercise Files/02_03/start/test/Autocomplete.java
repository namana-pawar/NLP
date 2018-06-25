import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;

public class Autocomplete {
    public static void main(String[] args) throws InterruptedException {

        System.setProperty("webdriver.chrome.driver", "/Users/namanapawar/Downloads/chromedriver");

        WebDriver driver = new ChromeDriver();

        driver.get("https://formy-project.herokuapp.com/autocomplete");

        WebElement autocomplete=driver.findElement(By.id("autocomplete"));
        autocomplete.sendKeys("738 West 27th street Los Angeles CA 90007");
        Thread.sleep(1000);
        WebElement autoCompleteResult=driver.findElement(By.className("pac-item"));
        autoCompleteResult.click();

        driver.quit();
    }
}
