import { StyleSheet, View } from 'react-native';
import PrimaryButton from './assets/components/PrimaryButton'
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Login from './pages/LoginScreen';
import Chat from './assets/components/Chat';
import Register from './pages/Register';
import SettingsScreen from './pages/SettingsScreen';
import LoadingScreen from './pages/LoadingScreen';

export default function App() {
  const Stack = createNativeStackNavigator();
  const Tab = createBottomTabNavigator();

  return (
    <View style={styles.container}>
        <Stack.Navigator>
          <Stack.Screen name="LoadingScreen" component={LoadingScreen} />
          <Stack.Screen name="Login" component={Login} />
          <Stack.Screen name="Chat" component={Chat} />
          <Stack.Screen name="Register" component={Register} />
        </Stack.Navigator>
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
