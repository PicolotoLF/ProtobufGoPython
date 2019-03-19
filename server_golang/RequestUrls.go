package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func makeRequest(url string, ch chan string) {
	resp, err := http.Get(url)

	if err != nil {
		fmt.Println("Error: ", err)
		bodyString := fmt.Sprintf("Request didn't work. GoLang error message: %s", err)
		ch <- bodyString
		return
	}
	defer resp.Body.Close()
	if resp.StatusCode == http.StatusOK {
		bodyBytes, _ := ioutil.ReadAll(resp.Body)
		bodyString := string(bodyBytes)
		ch <- bodyString
	} else {
		bodyString := fmt.Sprintf("Request return status: %d with message %s",
			resp.StatusCode, resp.Status)
		ch <- bodyString
	}

}

func getMlbs(urls []string) []string {
	const numOfResults := len(urls)

	fmt.Println(len(urls))
	var arrayResps [numOfResults]string
	ch := make(chan string, numOfResults)

	for _, url := range urls {
		go makeRequest(url, ch)
	}

	for i := 0; i < numOfResults; i++ {
		v, ok := <-ch
		arrayResps = append(arrayResps, v)
		// fmt.Println(arrayResps)
		if !ok {
			close(ch)
		}
		// fmt.Println(arrayResps)
	}
	fmt.Println(arrayResps)
	return arrayResps
}

func main() {
	urls := []string{"https://api.mercadolibre.com/items/MLB1150156997"}
	getMlbs(urls)
}
