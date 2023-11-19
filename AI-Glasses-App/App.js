import { StyleSheet, View } from 'react-native';
import PrimaryButton from './assets/components/PrimaryButton'
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import AppNavigator from './assets/components/AppNavigator'

export default function App() {

  return (
    <View style={styles.container}>
        <AppNavigator />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  heading: {
    fontSize: 24,
    marginBottom: 20,
  },
  input: {
    width: 200,
    height: 40,
    borderWidth: 1,
    borderColor: 'gray',
    marginBottom: 10,
    padding: 10
  },
  signupContainer: {
    marginTop: 5,
    alignItems: 'center',
    gap: 10,
    display: 'flex'
  },
});
