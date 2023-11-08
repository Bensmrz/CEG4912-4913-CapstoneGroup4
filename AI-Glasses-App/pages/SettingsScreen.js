import React, { useState } from 'react';
import { View, Text, Switch, TouchableOpacity, StyleSheet } from 'react-native';

function SettingsScreen() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('English');
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);

  const changeLanguage = (language) => {
    setSelectedLanguage(language);
  };

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text style={{ fontSize: 20, marginBottom: 16 }}>Settings</Text>

      <Text style={{ fontSize: 16, marginBottom: 8 }}>Theme</Text>
      <Switch
        value={isDarkMode}
        onValueChange={() => toggleTheme()}
      />

      <Text style={styles.themeText}>
        {isDarkMode ? 'Dark Mode' : 'Light Mode'}
      </Text>

      <Text style={{ fontSize: 16, marginBottom: 8 }}>Language</Text>
      <View style={{ flexDirection: 'row', marginBottom: 16 }}>
        <TouchableOpacity
          style={[
            styles.languageButton,
            selectedLanguage === 'English' && styles.selectedButton,
          ]}
          onPress={() => changeLanguage('English')}
        >
          <Text style={styles.buttonText}>English</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[
            styles.languageButton,
            selectedLanguage === 'French' && styles.selectedButton,
          ]}
          onPress={() => changeLanguage('French')}
        >
          <Text style={styles.buttonText}>French</Text>
        </TouchableOpacity>
      </View>

      <Text style={{ fontSize: 16, marginBottom: 8 }}>Notifications</Text>
      <Switch
        value={notificationsEnabled}
        onValueChange={(value) => setNotificationsEnabled(value)}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  themeText: {
    fontSize: 16,
    marginBottom: 8,
  },
  languageButton: {
    backgroundColor: 'blue',
    padding: 10,
    borderRadius: 8,
    margin: 4,
  },
  selectedButton: {
    backgroundColor: 'darkblue',
  },
  buttonText: {
    color: 'white',
  },
});

export default SettingsScreen;
