"""
Earthquake Detection App
"""
import get_data

if __name__ == "__main__":
    print("Main App")
    data = get_data.extract()
    get_data.show_data(data)
